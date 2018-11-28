#include <iostream>
#include <set>
#include <vector>
#include <fstream>
#include <algorithm>

double timeUntilGoal(double goal, double rate)
{
    return goal / rate;
}

double timeUntilGoalWithFarm(double goal, double cr, double fc, double ru)
{
    return timeUntilGoal(fc, cr) + timeUntilGoal(goal, cr + ru);
}

double doTick(double goal, double cr, double fc, double ru, double accu)
{
    double t = timeUntilGoal(goal, cr);
    double t_with_farm = timeUntilGoalWithFarm(goal, cr, fc, ru);
    if (t < t_with_farm)
        return accu + t;
    else
        return doTick(goal, cr + ru, fc, ru, accu + timeUntilGoal(fc, cr));
}

void validateTestCase(std::ifstream& stream, std::ofstream& out, int num)
{
    double farm_cost, farm_adder, goal;
    stream >> farm_cost >> farm_adder >> goal;
    double result = doTick(goal, 2, farm_cost, farm_adder, 0);
    out.precision(10);
    out << "Case #" << num << ": " << result << std::endl;
}

int main(int argc, char* argv[])
{
    std::ifstream read(argv[1]);
    int test_cases;
    read >> test_cases;

    std::ofstream outfile;
    outfile.open ("output.out");

    for (int i = 1; i <= test_cases; ++i)
        validateTestCase(read, outfile, i);

    outfile.close();
    return 0;
}
