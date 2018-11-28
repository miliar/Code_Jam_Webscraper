#include<iostream>
#include<vector>
#include <time.h> 
using namespace std;
vector<string> getW(string s)
{
        vector<string> subs; 
        string ws = "";
        ws += s[0];
        for(int i=1 ;i<s.size();i++)
        {
                if(s[i]!=s[i-1])
                {
                 subs.push_back(ws);
                 ws = "";
                }
                ws+=s[i];
        }
        subs.push_back(ws);
        
        return subs;
}
int main()
{
     freopen("A_out.txt","w",stdout);
     freopen("A-small-attempt0(1).in","r",stdin);
    int TT;
    cin>>TT; 
    for (int T = 1; T<=TT; T++)
    {
        int N;
        cin>>N;
        vector<string> strs;
        for(int i=0;i<N;i++)
        {
                string astr;
                cin>>astr;
                strs.push_back(astr);
        }
        vector<string>   subs1 = getW(strs[0]);
      
        vector<string>   subs2 = getW(strs[1]);
        
        bool isGood = true;
        int cnt =0;
        if(subs1.size()!=subs2.size())
        {
           isGood = false;
           
         }else {
             for(int i=0;i<subs1.size();i++)
             {
                     string s1 = subs1[i];
                     string s2 = subs2[i];
                     if(s1[0]!=s2[0])
                     {
                                     isGood = false;
                                     break;
                     }
                     int m = s1.size()-s2.size();
                     cnt += abs(m);
                     
             }
         }
         if(!isGood)
         {          
                cout<<"Case #"<<T<<": Fegla Won"<<endl;
         }else
            cout<<"Case #"<<T<<": "<<cnt<<endl;
    } 
    return 0;
    
}
