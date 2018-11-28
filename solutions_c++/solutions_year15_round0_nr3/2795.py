#include <iostream>
#include <cmath>
#include <map>
#include <sstream>
#include <algorithm>
using namespace std;
int main ()
{
    map<string,map<string,string> >mapping;
    mapping["i"]["i"]="-1";
      mapping["i"]["j"]="k";
    mapping["i"]["k"]="-j";
    mapping["i"]["1"]="i";
    mapping["i"]["-1"]="-i";
    
    mapping["-i"]["i"]="1";
      mapping["-i"]["j"]="-k";
    mapping["-i"]["k"]="j";
    mapping["-i"]["1"]="-i";
    mapping["-i"]["-1"]="i";
    
    mapping["j"]["i"]="-k";
      mapping["j"]["j"]="-1";
    mapping["j"]["k"]="i";
    mapping["j"]["1"]="j";
    mapping["j"]["-1"]="-j";
    
    mapping["-j"]["i"]="k";
      mapping["-j"]["j"]="1";
    mapping["-j"]["k"]="-i";
    mapping["-j"]["1"]="-j";
    mapping["-j"]["-1"]="j";
    
    mapping["k"]["i"]="j";
      mapping["k"]["j"]="-i";
    mapping["k"]["k"]="-1";
    mapping["k"]["1"]="k";
    mapping["k"]["-1"]="-k";
    
      mapping["-k"]["i"]="-j";
      mapping["-k"]["j"]="i";
    mapping["-k"]["k"]="1";
    mapping["-k"]["1"]="-k";
    mapping["-k"]["-1"]="k";
    
    mapping["1"]["i"]="i";
      mapping["1"]["j"]="j";
    mapping["1"]["k"]="k";
    mapping["1"]["1"]="1";
    mapping["1"]["-1"]="-1";
    
    mapping["-1"]["i"]="-i";
      mapping["-1"]["j"]="-j";
    mapping["-1"]["k"]="-k";
    mapping["-1"]["1"]="-1";
    mapping["-1"]["-1"]="1";
    int t;
    cin >> t;
    for (int t1(1);t1<=t;t1++)
    {

        int l,n;
        cin >> l >> n;
        string a,b("");
        cin >> a;
        for (int c(1);c<=n;c++)b+=a;
        int c(0);string prev("1");int i(0),j(0),k(0);
        for (;c<b.length();c++)
        {
            
            stringstream ss;
            ss<<b[c];
            string temp;ss>>temp;
            if (mapping[prev][temp]=="i"){c++;i=1;break;}
            else prev=mapping[prev][temp];
        }
        
        prev="1";
       
         for (;c<b.length();c++)
        {
             stringstream ss;
            ss<<b[c];
            string temp;ss>>temp;
            if (mapping[prev][temp]=="j"){c++;j=1;break;}
            else prev=mapping[prev][temp];
        }
        prev="1";
         for (;c<b.length();c++)
        {
             stringstream ss;
            ss<<b[c];
            string temp;ss>>temp;
            if (mapping[prev][temp]=="k"){c++;k=1;break;}
            else prev=mapping[prev][temp];
        }
        
        prev="1";
        for (;c<b.length();c++)
        {
            stringstream ss;
            ss<<b[c];
            string temp;ss>>temp;
          
            prev=mapping[prev][temp];
        }

        if (prev=="1"&&i==1&&j==1&&k==1)cout << "Case #" << t1 << ": " << "YES" << endl;
        else cout << "Case #" << t1 <<": " << "NO" << endl;
    }
    return 0;
}
