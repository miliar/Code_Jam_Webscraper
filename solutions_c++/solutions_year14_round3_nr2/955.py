#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<sstream>
#include<cmath>
#include<cstdio>
using namespace std;
#define REP(i,n) for(int i=0;i<n;++i)
#define REPD(i,n) for(int i=n;i>-1;--i)
#define FOR(i,j,k) for(int i=j;i<k;++i)
#define PB push_back
#define LL unsigned long long
#define MAX_S 101
#define MP make_pair
#define ALL(v) v.begin(),v.end()
#define INF 1000000000

bool check(vector<int> array,vector<string> & data)
{
		vector<int> ch(26,0);
		
		string tmp = "";

		REP(i,array.size()) tmp+=data[array[i]];
	//	cout<<tmp<<endl;		
		REP(j,tmp.size())
		{
			int next = j+1;
			
			if(next<tmp.size())
			{
//REP(i,26) cout<<ch[i]<<" ";cout<<endl;
			   if(tmp[next]!=tmp[j])
				{
				    if(ch[tmp[next]-'a']>0) {// cout<<j<<" "<<tmp<<endl; 
					return false; 	}
			    	else if(ch[tmp[next]-'a']==0) ch[tmp[j]-'a'] = 1; 
				}
			}
			else{ 
			//	REP(i,26) cout<<ch[i]<<" ";cout<<endl;
				if(tmp[j]==tmp[0] && ch[tmp[0]-'a']>0 ) return false;
                //   	if(ch[j]>0) {
				//	    cout<<"!"<<endl;
				//		REP(i,26) cout<<ch[i]<<" ";cout<<endl;
				//		return false;
                //   	}
			}

		}
	
	return true;
}

void perm(vector<int>  array, int start, int end, LL &count,vector<string> & data)
{
    if((end-start) == 1)
    {
	     if(check(array,data)) {
				++count;
		//		        for(int i=0;i<=end;i++)
       //     cout << array[i] << " ";
      //  cout << endl;
	     }
		


        swap(array[start],array[end]);

	     if(check(array,data)) {
				++count;
		//		      for(int i=0;i<=end;i++)
        //    cout << array[i] << " ";
       // cout << endl;
	     }

        swap(array[start],array[end]);

    }
    else
    {

        for(int i=start;i <=end;i++ )
        {
            swap(array[i],array[start]);
            perm(array,start+1,end,count,data);
            swap(array[i],array[start]);
        }
    }
}

int main(){
	 int ts=0; cin>>ts;
	 REP(ww,ts)
	 {
	    LL total = 0;
	    int n;cin>>n;
	    

	    
	    vector<string> data(n);REP(i,n) cin>>data[i];
	    vector<int> p(n); REP(i,n) p[i]=i;
	    perm(p,0,n-1,total,data);
	    if(n==1 && check(p,data) ) ++total; 

		cout<<"Case #"<<(ww+1)<<": "<<total<<endl;
	 }
	
	return 0;
}
