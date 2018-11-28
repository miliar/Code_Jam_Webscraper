#include <cmath>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <algorithm>
#include <stack>

using namespace std;

int main()
{
    freopen("C-small-practice.in","r", stdin);
    freopen("result.out","w", stdout);

    int T;
    int N,X,c1,c2=0,s1=0,c=0,c3=1,j;
    string s="";
    char a;

    cin>>T;
    for(int i=1;i<=T;i++)
    {
        c1 = 0;
        c2 = 0;
        c3=1;
        cin>>N>>X>>s;
        a = s.at(0);
        if(a == 'i')
        {
            c1++;
            j=2;
            a = s.at(1%N);
        }
        else
            j=1;

        for(;j<N*X;j++)
        {

            if(c1 == 0 && a == 'i' && c3 == 1)
            {
                //cout<<" "<<j;
                c1 = 1;
                a=s.at(j%N);
                //j++;
                continue;
            }
            else if(c1 == 1 && a == 'j' && c3 == 1)
            {
                //cout<<" "<<j;
                c1 = 2;
                a=s.at(j%N);
                //j++;
                continue;
            }
            else if(c1 == 2 && j <= (N*X-1))
            {
                if(a == '1' && s.at(j%N) == '1')
            {

                a = '1';
            }
            else if(a == '1' && s.at(j%N) == 'i')
            {

                a = 'i';
            }
            else if(a == '1' && s.at(j%N) == 'j')
            {

                a = 'j';
            }
            else if(a == '1' && s.at(j%N) == 'k')
            {

                a = 'k';
            }
            else if(a == 'i' && s.at(j%N) == '1')
            {

                a = 'i';
            }
            else if(a == 'i' && s.at(j%N) == 'i')
            {

                c3=c3*-1;
                a = '-1';
            }
            else if(a == 'i' && s.at(j%N) == 'j')
            {

                a = 'k';
            }
            else if(a == 'i' && s.at(j%N) == 'k')
            {

                 c3=c3*-1;
                a = '-j';
            }
            else if(a == 'j' && s.at(j%N) == '1')
            {

                a = 'j';
            }
            else if(a == 'j' && s.at(j%N) == 'i')
            {

                  c3=c3*-1;
                a = '-k';
            }
            else if(a == 'j' && s.at(j%N) == 'j')
            {

                  c3=c3*-1;
                a = '-1';
            }
            else if(a == 'j' && s.at(j%N) == 'k')
            {

                a = 'i';
            }
            else if(a == 'k' && s.at(j%N) == '1')
            {

                a = 'k';
            }
            else if(a == 'k' && s.at(j%N) == 'i')
            {

                a = 'j';
            }
            else if(a == 'k' && s.at(j%N) == 'j')
            {

                  c3=c3*-1;
                a = '-i';
            }
            else if(a == 'k' && s.at(j%N) == 'k')
            {

                  c3=c3*-1;
                a = '-1';
            }
            continue;

            }
            if(a == '1' && s.at(j%N) == '1')
            {

                a = '1';
            }
            else if(a == '1' && s.at(j%N) == 'i')
            {

                a = 'i';
            }
            else if(a == '1' && s.at(j%N) == 'j')
            {

                a = 'j';
            }
            else if(a == '1' && s.at(j%N) == 'k')
            {

                a = 'k';
            }
            else if(a == 'i' && s.at(j%N) == '1')
            {

                a = 'i';
            }
            else if(a == 'i' && s.at(j%N) == 'i')
            {

                  c3=c3*-1;
                  //a = '1';
                a = '-1';
                //cout<<a;
            }
            else if(a == 'i' && s.at(j%N) == 'j')
            {

                a = 'k';
            }
            else if(a == 'i' && s.at(j%N) == 'k')
            {

                 c3=c3*-1;
                a = '-j';
            }
            else if(a == 'j' && s.at(j%N) == '1')
            {

                a = 'j';
            }
            else if(a == 'j' && s.at(j%N) == 'i')
            {

                  c3=c3*-1;
                a = '-k';
            }
            else if(a == 'j' && s.at(j%N) == 'j')
            {

                  c3=c3*-1;
                a = '-1';
            }
            else if(a == 'j' && s.at(j%N) == 'k')
            {

                a = 'i';
            }
            else if(a == 'k' && s.at(j%N) == '1')
            {

                a = 'k';
            }
            else if(a == 'k' && s.at(j%N) == 'i')
            {

                a = 'j';
            }
            else if(a == 'k' && s.at(j%N) == 'j')
            {

                  c3=c3*-1;
                a = '-i';
            }
            else if(a == 'k' && s.at(j%N) == 'k')
            {

                  c3=c3*-1;
                a = '-1';
            }

        }


        if(a == 'k' && c3 == 1 && c1 == 2)
            c1 = 3;
        //cout<<"   "<<c1<<"   ";
        if(c1 == 3)
            cout<<"Case #"<<i<<": "<<"YES"<<"\n";
        else
            cout<<"Case #"<<i<<": "<<"NO"<<"\n";
    }

    fclose(stdout);
    fclose(stdin);
    return 0;
}
