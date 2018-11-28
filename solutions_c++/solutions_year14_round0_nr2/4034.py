#include<iostream>
#include<iomanip>
#include<fstream>

using namespace std;

int main()
{
    ofstream output;
    ifstream input ("B-large.in");
    output.open ("B-large.out");

    if(input.is_open())
    {
        int t;
        double c, f, x, time, in, oldTime, newTime;

        input >> t;
        for(int i = 0;i < t;i++)
        {
            in = 2;
            time = 0;
            input >> c >> f >> x;

            while(true)
            {
                oldTime = (x/in);
                newTime = (c/in)+(x/(in+f));
                if(oldTime > newTime)
                {
                    time += (c/in);
                    in += f;
                }
                else
                {
                    time += (x/in);
                    break;
                }
            }
            output << "Case #" << i + 1 << ": " << setprecision(7) << fixed << time << endl;
        }
        output.close();
    }

	return 0;
}
