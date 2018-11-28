#include<bits/stdc++.h>
#include<fstream>



#define ll long long
#define fin cin
#define fout cout

using namespace std;

ll t,d,p[200000],ans,buffer,cur,tmp;
string s;
priority_queue<ll> q;

int main(){
    ifstream fin("input.txt");
    //ofstream fout("output.txt");

    fin>>t;
    for( ll ca = 1; ca <= t; ca++ ) {
        fin>>d;
        cout<<"d:"<<d<<endl;

        while(!q.empty())q.pop();

        for( ll i = 0; i < d; i++ ) {
            fin>>p[i];
            //cout<<"\ti:"<<i<<"\tval:"<<p[i]<<endl;
            q.push(p[i]);
        }

        ans=q.top();

        buffer=0;

        while(q.top()!=1){
            cur=q.top();
            q.pop();



            q.push(cur/2);
            if(cur%2){
                q.push((cur/2)+1);
                //buffer++;
            }
            else{
                q.push(cur/2);
            }
            buffer++;

            tmp = min( cur + buffer - 1,q.top() + buffer );
            //cout<<"\t\t\ttmp:"<<tmp<<"\ttop:"<<q.top()<<endl;
            ans = min( ans, tmp );
            cout<<"\t\t\ttmp:"<<tmp<<"\ttop:"<<q.top()<<"\tans:"<<ans<<"\tbuffer:"<<buffer<<"\tcur:"<<cur<<endl;

        }

        fout<<"Case #"<<ca<<": "<<ans<<"\n";
    }
    return 0;
}

