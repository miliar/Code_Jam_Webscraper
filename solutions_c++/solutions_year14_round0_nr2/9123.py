// cookieClicker.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;



class solver
{
public:
    const int defaultRate = 2;
    solver(double cost, double rate, double goal)
        : m_cost(cost),
        m_rate(rate),
        m_goal(goal)
    {
        
    };

    /// returns the time to reach the goal
    double solve()
    {
        double totalTime = 0;
        double farmCount = 0;

     //   double timeToGoal = DBL_MAX;
       // double timeToFarm = 0;

        double timeToGoal = m_goal / (defaultRate + m_rate*farmCount);
        double timeToFarm = m_cost  / (defaultRate + m_rate*farmCount);
        double timeToGoalwithFarm = timeToFarm + m_goal  / (defaultRate + m_rate*(1 + farmCount));

        while (timeToGoal > timeToGoalwithFarm)
        {
            //cookieCount -= m_cost;
            ++farmCount;
            totalTime += timeToFarm;

            timeToGoal = m_goal  / (defaultRate + m_rate*farmCount);
            timeToFarm = m_cost / (defaultRate + m_rate*farmCount);
            timeToGoalwithFarm = timeToFarm + m_goal / (defaultRate + m_rate*(1 + farmCount));
        }

        totalTime += timeToGoal;

        return totalTime;
    }


private:
    double m_cost;
    double m_rate;
    double m_goal;

};


void solvePuzzle()
{
    double C = 0; /// farm cost
    double F = 0; /// farm production rate
    double X = 0; /// win condition

    cin >> C >> F >> X;

    solver temp(C, F, X);

    cout << temp.solve() << endl;
}


int _tmain(int argc, _TCHAR* argv[])
{
    int T = 0; /// num test cases


    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        cout << std::setprecision(10) << "Case #" << i + 1 << ": ";
        solvePuzzle();

    }

	return 0;
}

