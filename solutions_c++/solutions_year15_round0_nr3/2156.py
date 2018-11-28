#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
void initialisation(vector < vector < pair <char,char> > > &Multiplying)
{
    Multiplying[1][1]={'+','h'};
    Multiplying[2][2]={'-','h'};
    Multiplying[3][3]={'-','h'};
    Multiplying[4][4]={'-','h'};
    Multiplying[1][2]={'+','i'};
    Multiplying[1][3]={'+','j'};
    Multiplying[1][4]={'+','k'};
    Multiplying[2][1]={'+','i'};
    Multiplying[3][1]={'+','j'};
    Multiplying[4][1]={'+','k'};
    Multiplying[2][3]={'+','k'};
    Multiplying[2][4]={'-','j'};
    Multiplying[3][2]={'-','k'};
    Multiplying[3][4]={'+','i'};
    Multiplying[4][2]={'+','j'};
    Multiplying[4][3]={'-','i'};
}
void testcase_brutal_dijikstra(int t)
{
    int L; int X;
    cin >> L;
    cin >> X;
    string s; string c;
    cin >> s;
    c=s;
    for(int x=1; x<X; x++)
        c=c+s;
    vector < vector < pair <char,char> > > Multiplying(5, vector < pair <char,char> > (5));
    initialisation(Multiplying);
    int minuses1=0; bool answer_found=false; char first1='h';  pair <char,char> r; r={'+','k'};            //char 'h' means '1';
    vector < pair <char,char> > Sufixes(X*L); vector <int> To_choose;
    Sufixes[X*L-1]={'+',c[X*L-1]};
    if(Sufixes[X*L-1]==r)
        To_choose.push_back(X*L-1);
    for(int f=X*L-2; f>1; f--)
        {
            char signum=Sufixes[f+1].first;
            if(Multiplying[c[f]-'g'][Sufixes[f+1].second-'g'].first=='-')
                {
                    if(signum=='+')
                        signum='-';
                    else
                        signum='+';
                }
            Sufixes[f]={signum,Multiplying[c[f]-'g'][Sufixes[f+1].second-'g'].second};
            //cout << Sufixes[f].first << " " << Sufixes[f].second <<endl;
            if(Sufixes[f]==r)
                {
                    To_choose.push_back(f);
                    //cout << "To_choose: " << f <<endl;
                }
        }
    reverse(To_choose.begin(),To_choose.end()); int last=0;
    for(int i=0; i<L*X-2 && !answer_found; i++)
        {
            if(Multiplying[first1-'g'][c[i]-'g'].first=='-')
                minuses1=(minuses1+1)%2;
            first1=Multiplying[first1-'g'][c[i]-'g'].second;
            //cout << first1 << " " << minuses1 <<endl;
            if(minuses1==0 && first1=='i')
                {
                    //cout << "i=" << i << " " << minuses1 << "  " << first1 <<endl;
                    int minuses2=0; char second2='h'; int j=i+1;
                    for(int b=last; b<To_choose.size() && !answer_found; b++)
                        if(To_choose[b]>i+1)
                        {
                            last=b;
                            //cout << To_choose[b] <<endl;
                            while(j<=To_choose[b]-1)
                                {
                                    if(Multiplying[second2-'g'][c[j]-'g'].first=='-')
                                        minuses2=(minuses2+1)%2;
                                    second2=Multiplying[second2-'g'][c[j]-'g'].second;
                                    j++;
                                }
                            //cout << "j=" << j << " " << minuses2 << " " << second2 <<endl;
                                if(minuses2==0 && second2=='j')
                                    answer_found=true;
                        }
                }
        }
    if(answer_found)
        cout << "Case #" << t << ": YES" <<endl;
    else
        cout << "Case #" << t << ": NO" <<endl;
}
int main ()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
        testcase_brutal_dijikstra(t);
    return 0;
}
