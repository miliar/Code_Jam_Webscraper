#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream inin;
    inin.open("C:\\WYX\\A-small-attempt2.in",ios::in);
    ofstream outt;
    outt.open("C:\\WYX\\A-small-out.out",ios::out);
    int num;
    inin >> num;
    for (int kk=0;kk<num;kk++)
    {
        int people;
        char a[1010];
        inin >> people >> a;
        people++;
        int add = 0, sum = 0;
        for (int i=0;i<people;i++)
        {
            int k = int(a[i])-48;
            if (sum<i)
            {
                add = add+i-sum;
                cout << i << " " << sum << " " << add << endl;
                sum = i;
            }
            sum = sum+k;
        }
        outt << "Case #" << kk+1 << ": " << add << endl;

       // return 0;
    }
}
