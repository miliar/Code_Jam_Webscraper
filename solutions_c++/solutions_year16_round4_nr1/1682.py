#include <bits/stdc++.h>

using namespace std;

int main(){
	int t,k=1,i,j;
	streambuf *coutbuf =  cout.rdbuf();
    streambuf *cinbuf =  cin.rdbuf();

    ofstream out("ans.txt");
     ifstream in("A-small-attempt2.in");

  //  Read from infile.txt using  cin
    cin.rdbuf(in.rdbuf());

    //Write to outfile.txt through  cout
 cout.rdbuf(out.rdbuf());
	cin>>t;
	while(t--){
        int n,r,p,s,tr,tp,ts;
        string prev[3],next[3];
        cin>>n>>tr>>tp>>ts;
        bool flag[3] = {true,true,true};
        cout<<"Case #"<<k++<<": ";
        int x,y=0;
        string xyz ="PRS";
        //cout<<prev[y]<<endl;
        for(y=0;y<3;++y){
                prev[y].push_back(xyz.at(y));
                   p =tp;
                r= tr;
                s =ts;
                if(y==0 && !p){
                    flag[y]=false;
                    continue;
                }
                                if(y==1 && !r){
                    flag[y]=false;
                    continue;
                }
                                if(y==2 && !s){
                    flag[y]=false;
                    continue;
                }
                if(y==0)
                    p--;
                if(y==1)
                    r--;
                if(y==2)
                    s--;
            //cout<<prev[y]<<endl;
        if(prev[y].length()>0){
        for(i=0;i<n-1;++i){
            x = pow(2,i);
            for(j=0;j<x;++j){
                if(prev[y].at(j)=='P'){
                    next[y].push_back('P');
                    if(!r)
                    {
                        flag[y]=false;
                        break;
                    }
                    r--;
                    next[y].push_back('R');
                }
                if(prev[y].at(j)=='R'){
                    if(!s)
                    {
                        flag[y]=false;
                        break;
                    }
                    s--;
                    next[y].push_back('S');
                    next[y].push_back('R');
                }
                if(prev[y].at(j)=='S' ){
                    if(!p)
                    {
                        flag[y]=false;
                        break;
                    }
                    p--;
                    next[y].push_back('S');
                    next[y].push_back('P');
                }

            }
            if(!flag[y])
                break;
            prev[y] = next[y];
            next[y].clear();
        }
        x = pow(2,n-1);
       // cout<<x<<" "<<prev[y]<<endl;
        if(flag[y]){
        for(j=0;j<x;++j){
               if(prev[y].at(j)=='P'){
                    next[y].push_back('P');
                    if(r<=0)
                    {
                        flag[y]=false;
                        break;
                    }
                    r--;
                    next[y].push_back('R');
                }
                if(prev[y].at(j)=='R'){
                    next[y].push_back('R');
                    if(s<=0)
                    {
                        flag[y]=false;
                        break;
                    }
                    s--;

                    next[y].push_back('S');
                }
                if(prev[y].at(j)=='S' ){
                   next[y].push_back('P');
                    if(p<=0)
                    {
                        flag[y]=false;
                        break;
                    }
                    p--;

                    next[y].push_back('S');
                }

            }
        }
        }
          //  cout<<next[y]<<endl;
        }
        sort(next,next+3);
        for(i=0;i<3;++i){
            if(next[i].length()==pow(2,n) && flag[y]){
                cout<<next[i];
                break;
            }
        }
        if(i==3)
            cout<<"IMPOSSIBLE";
        cout<<endl;

        }



cin.rdbuf(cinbuf);
    cout.rdbuf(coutbuf);
	return 0;
}
