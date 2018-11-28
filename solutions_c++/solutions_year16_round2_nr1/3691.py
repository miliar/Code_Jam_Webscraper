#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
      //ios::sync_with_stdio(false);
      freopen("jamin2.txt","r",stdin);
      freopen("jamout2.txt","w",stdout);

    int test;
    cin >> test;
    for(int i=1;i<=test;i++)
    {
          string s;
          cin >> s;
          map<char,int> mymap;
          char c='A';
          vector<int>v(10);

          for(int j=0;j<10;j++)
          {
              v[j]=0;
          }
          //
          for(int j=0;j<26;j++)
          {

              mymap[c]=0;
              c++;
          }

          for(int j=0;j<s.size();j++)
          {
              mymap[s[j]]+=1;
          }

          for(int jp=0;jp<s.size();jp++)
          {

          if(mymap['W']>0)
          {
              v[2]+=1;
              mymap['T']-=1;
              mymap['W']-=1;
              mymap['O']-=1;
          }
          else if(mymap['X']>0)
          {
              v[6]+=1;
              mymap['S']-=1;
              mymap['I']-=1;
              mymap['X']-=1;
          }
          else if(mymap['Z']>0)
          {
              v[0]+=1;
              mymap['Z']-=1;
              mymap['E']-=1;
              mymap['R']-=1;
              mymap['O']-=1;
          }
          else if(mymap['G']>0)
          {
              v[8]+=1;
              mymap['E']-=1;
              mymap['I']-=1;
              mymap['G']-=1;
              mymap['H']-=1;
              mymap['T']-=1;
          }
          else if(mymap['U']>0)
          {
              v[4]+=1;
              mymap['F']-=1;
              mymap['O']-=1;
              mymap['U']-=1;
              mymap['R']-=1;
         }
          else if(mymap['U']>0)
          {
              v[4]+=1;
              mymap['F']-=1;
              mymap['O']-=1;
              mymap['U']-=1;
              mymap['R']-=1;
         }
          else if(mymap['H']>0)
          {
              v[3]+=1;
              mymap['T']-=1;
              mymap['H']-=1;
              mymap['R']-=1;
              mymap['E']-=1;
              mymap['E']-=1;
         }

          else if(mymap['F']>0)
          {
              v[5]+=1;
              mymap['F']-=1;
              mymap['I']-=1;
              mymap['V']-=1;
              mymap['E']-=1;
         }

          else if(mymap['V']>0)
          {
              v[7]+=1;
              mymap['S']-=1;
              mymap['E']-=1;
              mymap['V']-=1;
              mymap['E']-=1;
              mymap['N']-=1;
         }

          else if(mymap['O']>0)
          {
              v[1]+=1;
              mymap['O']-=1;
              mymap['N']-=1;
              mymap['E']-=1;
         }
         else if (mymap['N']>0)
         {
             v[9]+=1;

              mymap['N']-=1;
              mymap['I']-=1;
              mymap['N']-=1;
              mymap['E']-=1;

         }
    }

         int yy=0;
            for(int kk=1;kk<10;kk++)
            {
                if( v[kk]>0 ){
                int z=v[kk];
                for(int pp=0;pp<z;pp++)
                {
                  yy=yy*10+kk;
                }
                }

            }
            cout << "Case #" << i << ": " ;
            if(v[0]>0)
            {
                //cout << "dasfs " << v[0] <<"  ";
                int as=v[0];
                for(int kkk=0;kkk<as;kkk++)
                {
                    cout<<"0" ;
                }


            }
            if(yy>0)
            cout << yy << endl;
            else
            cout << "\n";

    }

    return 0;
}
