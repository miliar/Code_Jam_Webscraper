#include<bits/stdc++.h>


using namespace std;

int f[130];

vector<pair<int,char> >order;
vector<string>name;

void init(){
    order.push_back(make_pair(0,'Z'));
    order.push_back(make_pair(8,'G'));
    order.push_back(make_pair(6,'X'));
    order.push_back(make_pair(4,'U'));
    order.push_back(make_pair(5,'F'));
    order.push_back(make_pair(3,'H'));
    order.push_back(make_pair(2,'T'));
    order.push_back(make_pair(1,'O'));
    order.push_back(make_pair(7,'V'));
    order.push_back(make_pair(9,'I'));
    name.push_back("ZERO");
    name.push_back("ONE");
    name.push_back("TWO");
    name.push_back("THREE");
    name.push_back("FOUR");
    name.push_back("FIVE");
    name.push_back("SIX");
    name.push_back("SEVEN");
    name.push_back("EIGHT");
    name.push_back("NINE");
}


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    string s;
    cin>>T;
    init();
    for(int t=1;t<=T;t++){
        cin>>s;
        memset(f,0,sizeof(f));
        vector<int>res;
        for(int i=0;i<s.length();i++){
            f[ s[i] ] ++;
        }
        for(int i=0;i<order.size();i++){
            int num = order[i].first;
            char ch = order[i].second;
            while( f[ch] ){
                res.push_back(num);
                for(int j=0;j<name[num].length();j++)--f[name[num][j]];
            }
        }
        sort(res.begin(),res.end());
        printf("Case #%d: ",t);
        for(int i=0;i<res.size();i++)cout<<res[i];
        cout<<endl;
    }
    return 0;
}
