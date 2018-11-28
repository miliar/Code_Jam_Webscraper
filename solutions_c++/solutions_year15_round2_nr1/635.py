#include <iostream>
#include <queue>
#include <cmath>
#include <iterator>
#include <algorithm>
#include <fstream>
#include <set>
#include <sstream>
#include <ctime>
#include <map>
using namespace std;

long long toInt(string s)
{
    stringstream ss;
    ss<<s;
    long long res;
    ss>>res;
    return res;
}


string decr(string s)
{
    stringstream ss;
    ss<<s;
    long long z;
    ss>>z;
    z--;
    ss.clear();
    ss<<z;
    ss>>s;
    return s;
}


int main()
{
    ios_base::sync_with_stdio(false);
    ifstream in("input.txt");
    ofstream out("output.txt");
    #define cin in
    #define cout out
    int nb_cas;
    cin>>nb_cas;

    for(int cas=1;cas<=nb_cas;cas++)
    {
        cout<<"Case #"<<cas<<": ";

        string N;
        cin>>N;

        long long res = 0;

        while(N!="0")
        {
            //cout<<N<<" "<<res<<endl;
            if(N.size()==1)
            {
                res += N[0]-'0';
                break;
            }

            if(true)
            {
                //cout<<"lol "<<res<<endl;
                if(N[N.size()-1]!='0')
                {
                    long long pow10 = 10;
                    bool r = false;
                    if(N[0] > '1')
                    {
                        r = true;
                        res+=N[0]-'1';
                        N[0]='1';
                    }
                    if(N[N.size()-1]>'1')
                    {
                        res+=N[N.size()-1]-'1';
                        N[N.size()-1]='1';
                    }
                    for(int c=1;c<N.size()/2;c++)
                    {
                        if(N[c]!='0') r=true;
                        res+=(N[c]-'0')*pow10;
                        pow10*=10;
                        N[c]='0';
                    }
                    if(r) res++;
                    pow10=10;
                    for(int c=1;c<N.size()/2;c++)
                    {
                        res+=(N[N.size()-1-c]-'0')*pow10;
                        pow10*=10;
                        N[N.size()-c-1]='0';
                    }

                    if(N.size()%2==1)
                    {
                        res+=(N[N.size()/2]-'0')*pow10;
                        N[N.size()/2]='0';
                    }
                    string newNine = string(N.size()-1,'9');
                    res+=toInt(N)-toInt(newNine);
                    N = newNine;
                }
                else
                {
                    res++;
                    N = decr(N);
                }
                //cout<<N<<" "<<res<<endl;


            }
        }


        cout<<res<<endl;
    }
}
