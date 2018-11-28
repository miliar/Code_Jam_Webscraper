#include <iostream>
#include <algorithm>
#include <vector>
#include<string>
#include<cstring>
#include <stdio.h>


using namespace std;
vector<int>ans;
int findf(string s, char z){
	int n = 0;
	for(int i=0;i<s.length();i++)if(s[i]==z)n++;
	return n;
}
void exr(int n, string &s, string d){
	for(int k=0;k<d.length();k++)
	for(int i=0;i<n;i++){
            	std::size_t found = s.find(d[k]);
            	s.erase(found,1);

            }
}
int main()
{
    freopen("in.txt", "r",stdin );
    freopen("out.txt", "w",stdout );
    int tt;cin>>tt;
    string s;

    for(int t=1;t<=tt;t++){
        cin>>s;
        ans.clear();
        bool check[s.length()];
        //0
        int n = findf(s,'Z');
        for(int i=0;i<n;i++)ans.push_back(0);
        exr(n,s,"ZERO");
        //2
        n = findf(s,'W');
        for(int i=0;i<n;i++)ans.push_back(2);
        exr(n,s,"TWO");

        //4
        n = findf(s,'U');
        for(int i=0;i<n;i++)ans.push_back(4);
        exr(n,s,"FOUR");
        //6
        n = findf(s,'X');
        for(int i=0;i<n;i++)ans.push_back(6);
        exr(n,s,"SIX");
        //8
        n = findf(s,'G');
        for(int i=0;i<n;i++)ans.push_back(8);
        exr(n,s,"EIGHT");
        //1
        n = findf(s,'O');
        for(int i=0;i<n;i++)ans.push_back(1);
        exr(n,s,"ONE");

        //3
        n = findf(s,'H');
        for(int i=0;i<n;i++)ans.push_back(3);
        exr(n,s,"THREE");
        //5
        n = findf(s,'F');
        for(int i=0;i<n;i++)ans.push_back(5);
        exr(n,s,"FIVE");
        //7
        n = findf(s,'S');
        for(int i=0;i<n;i++)ans.push_back(7);
        exr(n,s,"SEVEN");

        n = findf(s,'I');
        for(int i=0;i<n;i++)ans.push_back(9);
        exr(n,s,"NINE");

        sort(ans.begin(),ans.end());




        cout<<"Case #"<<t<<": ";
        for(int i=0;i<ans.size();i++)cout<<ans[i];cout<<"\n";
        //cout<<s<<"\n";
    }
    return 0;
}
