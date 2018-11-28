#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
bool found(map<char,int>h,string s)
{
  for(int i=0;i<s.size();i++)
       if(h[s[i]])h[s[i]]--;
       else
       return false;

       return true;
}
void del(map<char,int>& h,string s)
{
   for(int i=0;i<s.size();i++)
        {
           h[s[i]]--;

        }

}
bool p(map<char,int>h)
{
  if(h.size()==0)
    return false;
    return true;
}
int main()
{
    freopen("in-large","r",stdin);
    freopen("out","w",stdout);

    int t;
    scanf("%d",&t);
    string str;
    string dic[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

       int vi[]={0,8,6,2,4};
       int afi[]={1,3,5,7,9};

     vector<pair<char,string> >v;
     v.push_back(make_pair('Z',dic[0]));

      v.push_back(make_pair('G',dic[8]));
       v.push_back(make_pair('X',dic[6]));
        v.push_back(make_pair('W',dic[2]));
         v.push_back(make_pair('U',dic[4]));


         vector<pair<char,string> >af;
         af.push_back(make_pair('O',dic[1]));
          af.push_back(make_pair('T',dic[3]));
           af.push_back(make_pair('F',dic[5]));
            af.push_back(make_pair('S',dic[7]));
            af.push_back(make_pair('N',dic[9]));
    for(int test=1;test<=t;test++)
    {
      printf("Case #%d: ",test);
       cin>>str;

      map<char,int>h;


       int n=str.size();

         for(int i=0;i<n;i++)h[str[i]]++;


         vector<int>ans;

          for(int i=0;i<v.size();i++)
             {
               if(h[v[i].first])
                  {
                  // cout<<v[i].first<<endl;
                    while(h[v[i].first])
                    {
                    ans.push_back(vi[i]);
                    del(h,v[i].second);
                    }

                  }
             }

             for(int i=0;i<af.size();i++)
             {
               if(h[af[i].first])
                  {
                    while(h[af[i].first])
                    {
                    ans.push_back(afi[i]);
                    del(h,af[i].second);
                    }

                  }
             }

              sort(ans.begin(),ans.end());
              for(int i=0;i<ans.size();i++)
              cout<<ans[i];
              cout<<endl;
    }
    return 0;
}
