
#include<fstream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream in;
ofstream out;
in.open("INPUT.in");
out.open("OUTPUT.txt");

int n;
    in>>n;
    int i=1;
    while(i<=n)
    {
     int sz;
     in>>sz;
     vector<pair<int,char> > vec;
for(int j=0;j<sz;j++)
{int a;in>>a;
    vec.push_back(make_pair(a,(char)('A'+j)));
}

out<<"Case #"<<i<<": ";

     sort(vec.begin(),vec.end(), greater<pair<int,char> >());
while(vec[0].first>0)
{
    if(vec[0].first-vec[1].first==vec[1].first-vec[2].first)
    {out<<vec[0].second<<" ";
        vec[0].first--;


    }
else{
    if(vec[0].first-vec[1].first>=2)
{out<<vec[0].second<<vec[0].second<<" ";
    vec[0].first=vec[0].first-2;
}
else{
    out<<vec[0].second<<vec[1].second<<" ";
   vec[0].first--;
    vec[1].first--;
}
}
 sort(vec.begin(),vec.end(), greater<pair<int,char> >());

    //cout<<" "<<vec[j].first<<" "<<vec[j].second;
}

out<<endl;
    i++;
    }
}
