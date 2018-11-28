#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
ifstream fin("D-large.in");
ofstream fout("output.out");
int T, n, s1, s2, s3, m;
double *p1, *p2, *temp;
bool flag;
int main()
{
    fin>>T;
    for(int i =0; i< T; i++)
    {
            fin>>n;s2 = 0;s1 = 0;s3 = 0;
            p1 = new double[n]();
            p2 = new double[n]();
            temp = new double[n]();
            for(int j =0; j< n; j++) fin>>p1[j];
            for(int j =0; j< n; j++) fin>>p2[j];
            sort(p1, p1+n);
            sort(p2, p2+n);
            for(int j =0; j< n; j++) temp[j] = p2[j];
            m = n-1;
            for(int j = n-1; j>= 0; j--)
            {
                    if(p1[m] > p2[j])
                    {
                             s3++;
                             m--;
                    }
            }
            for(int j =0; j< n; j++)
            {
                    if(p1[j] > p2[n-1]) s1++;
                    else
                    {
                        p2[n-1] = -1;
                        sort(p2, p2+n);
                    }
            }
            for(int j =0; j< n; j++)
            {
                    flag = 0;
                    for(int k = j; k< n; k++)
                    {
                            if(temp[k] > p1[j])
                            {
                                     flag = 1;
                                     temp[k] = -1;
                                     sort(temp, temp+n);
                                     break;
                            }
                    }
                    if(flag == 0) s2++;
            }
            fout<<"Case #"<<i+1<<": "<<max(s1, s3)<<" "<<s2<<"\n";
    }
    return 0;
}
