#include<iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    freopen("D:\\A-small-attempt4.in","r",stdin);
	freopen("D:\\b.out","w",stdout);
    int T;
    cin >> T;
    for(int x = 1 ; x <= T ; x++)
    {
        int Smax,fr = 0,sum = 0;
        string people;
        cin >> Smax;
        cin >> people;
        sum = int(people[0] - 48);

        for(int i = 1 ; i <= Smax ; i++)
        {
            if(i - sum > 0 and people[i] - 48 > 0)
            {
                fr += (i - sum);
                sum += fr;
                //cout << "(i)" << i << endl;
            }

            sum += int(people[i] - 48);

            //cout <<"(sum)"<< sum << endl<<endl;
        }

        cout << "Case #" << x <<": "<<fr << endl;

    }
    fclose(stdin);
	fclose(stdout);
	return 0;
}
