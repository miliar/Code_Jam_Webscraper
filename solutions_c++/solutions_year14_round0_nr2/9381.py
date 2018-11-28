#include <iostream>
#include <iomanip>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;
vector<double>  my_vector;
vector<double>  my_vector2;

double function(double C, double gain, double goal, double rate) {
    double time_cost;
    time_cost = goal/rate;
    double time_cost2,total;
    double gain_time;
    my_vector2.push_back(time_cost);
    gain_time =(double)(goal/(rate+gain)); 
    time_cost2 = double(C/rate) + gain_time;
    if(time_cost > time_cost2) {
        rate = gain+rate;
        my_vector.push_back(time_cost2-gain_time);
        function(C,gain,goal,rate);
    }
    return time_cost2;

}

int main() {

    double sum,hello;
    string line,line1;
    int xx =1;
    ifstream pFile ("small.in");
    if (pFile.is_open())
    {
        getline(pFile, line1);
        stringstream ss1(line1);
        ss1 >> hello;
        for(int i =0;i<hello;i++) { 
            double C= 0.0;
            double gain =0.0;
            double goal = 0.0;

            getline(pFile, line);
            stringstream ss(line);
            while(ss >> C >> gain >> goal)
            {
                function(C,gain,goal,2.0);
                for(int i=0;i<my_vector.size();i++)
                    sum = sum+my_vector[i];
                sum = sum+my_vector2[my_vector2.size()-1];
                cout << "Case #"<< xx << ": " <<  fixed << setprecision(7) << sum << endl;
                my_vector2.clear();
                my_vector.clear();
                sum =0;
                xx++;
            }

        }
        pFile.close();
    }
    else
        cout << "unable to open file " << endl;
}
