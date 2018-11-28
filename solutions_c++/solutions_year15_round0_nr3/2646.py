#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream inin;
    inin.open("C:\\WYX\\C-small-attempt0.in",ios::in);
    ofstream outout;
    outout.open("C:\\WYX\\dijstra.out",ios::out);
    int num;
    int table[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
    inin >> num;
    for (int all=0;all<num;all++)
    {
        int l,k;
        inin >> l >> k;
        char p[10002];
        int a[10002];
        inin >> p;
        for (int i=0;i<l*k;i++)
        {
            char m = p[i%l];
            if (m=='1') a[i] = 1;
            if (m=='i') a[i] = 2;
            if (m=='j') a[i] = 3;
            if (m=='k') a[i] = 4;
        }
        int point = 0, cal = 1, flag = 0;
        l = l*k;
        while (point<l)
        {
            if (cal>0) cal = table[cal][a[point]];
            else cal = -table[-cal][a[point]];
            if (cal==2 && flag==0)
            {
                flag = 1;
                cal = 1;
            }
            else if (cal==3 && flag==1)
            {
                flag = 2;
                cal = 1;
            }
            point++;
        }
        if (flag!=2 || cal!=4) outout << "Case #" << all+1 << ": NO" << endl;
        else outout <<  "Case #" << all+1 << ": YES" << endl;
    }
}
