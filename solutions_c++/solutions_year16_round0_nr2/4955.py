/*
#include <bits/stdc++.h>

typedef struct cords cords;

using namespace std;

struct cords
{
	lli y1,y2;
};
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <stdio.h>
//#include <pair>


using namespace std;
typedef long long int lli;
typedef unsigned int ui;
typedef unsigned long long int ulli;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define loop2(i,size) for(ui i=0;i<size;i++)
#define loop(i,begin,end) for(ui i=begin;i<=end;i++)

int main(){
	FILE *fp=fopen("2_lg_out.txt","w");
	int t,i=0,j=0,ans;
	vector<char> myv;
	string mys;
	cin>>t;
	while(i++ < t){
		j=0;
		ans=0;
		cin>>mys;
		myv=vector<char>(all(mys));
		while( (j< myv.size()) && (myv[j]=='-') ){
			j++;
		}
		if(j==0){ans=0;}
		else{ans=1;}

		while( j< myv.size() ){
			while( (j< myv.size()) && (myv[j]=='+') ){
				j++;
			}
			if(j==myv.size()){ break;}
			while( (j< myv.size()) && (myv[j]=='-') ){
				j++;
			}
			ans +=2;
		}


		cout<<"Case #"<<i<<": "<<ans<<endl;
		fprintf(fp,"Case #%d: %d\n",i,ans);
		
	}
	fclose(fp);
	return 0;
}