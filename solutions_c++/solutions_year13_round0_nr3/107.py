#include<cstdio>
#include<string>
#include<utility>
#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

typedef pair<int,int> P;

vector<string> palin;

vector<P> topalin(vector<P> vec,int hln,bool odd,int mid)
{
	vector<P> res;
	int sz=vec.size();
	for(int i=0;i<sz;i++) res.push_back(vec[i]);
	if(odd&&mid!=0) res.push_back(P(hln,mid));
	if(odd)
	{
		for(int i=0;i<sz;i++)
		{
			int d=vec[i].first,num=vec[i].second;
			res.push_back(P(2*hln-d,num));
		}
	}
	else
	{
		for(int i=0;i<sz;i++)
		{
			int d=vec[i].first,num=vec[i].second;
			res.push_back(P(2*hln-1-d,num));
		}
	}
	return res;
}

string db(vector<P> vec)
{
	string res;
	for(int i=0;i<120;i++) res+='0';
	for(int i=0;i<vec.size();i++) for(int j=0;j<vec.size();j++)
	{
		int d1=vec[i].first,d2=vec[j].first;
		int num1=vec[i].second,num2=vec[j].second;
		res[119-d1-d2]+=(num1*num2);
	}
	//palin.push_back(res);
	return res;
}

void get(vector<P> vec,int hln,bool odd,int mid)
{
	vector<P> num=topalin(vec,hln,odd,mid);
	string str=db(num);
	palin.push_back(str);
}

void prepare()
{
	string str;
	for(int i=0;i<120;i++) str+='0';
	str[119]='1';
	palin.push_back(str);
	str[119]='4';
	palin.push_back(str);
	str[119]='9';
	palin.push_back(str);
	vector<P> two;
	two.push_back(P(0,2));
	for(int hln=1;hln<=25;hln++)
	{
		//vector<P> vec=topalin(two,i,true,0);
		//palin.push_back(db(vec));
		get(two,hln,true,0);
		//vec=topalin(two,i,true,1);
		//db(vec);
		get(two,hln,true,1);
		//vec=topalin(two,i,false,0);
		//db(vec);
		get(two,hln,false,0);
		vector<P> vec;
		vec.push_back(P(0,1));
		for(int t=0;t<=2;t++) get(vec,hln,true,t);
		get(vec,hln,false,0);
		for(int i1=1;i1<hln;i1++)
		{
			vec.push_back(P(i1,1));
			for(int t=0;t<=2;t++) get(vec,hln,true,t);
			get(vec,hln,false,0);
			for(int i2=i1+1;i2<hln;i2++)
			{
				vec.push_back(P(i2,1));
				for(int t=0;t<=1;t++) get(vec,hln,true,t);
				get(vec,hln,false,0);
				for(int i3=i2+1;i3<hln;i3++)
				{
					vec.push_back(P(i3,1));
					for(int t=0;t<=1;t++) get(vec,hln,true,t);
					get(vec,hln,false,0);
					vec.pop_back();
				}
				vec.pop_back();
			}
			vec.pop_back();
		}
	}
}

int getcnt(string str)
{
	return distance(palin.begin(),upper_bound(palin.begin(),palin.end(),str));
}

int main()
{
	prepare();
	sort(palin.begin(),palin.end());
//	for(int i=0;i<40;i++) cout<<palin[i].substr(100,100)<<"\n";
	int T;
	cin>>T;
	for(int datano=0;datano<T;datano++)
	{
		string A,B;
		cin>>A>>B;
		int aln=A.size();
		for(int i=0;i<120-aln;i++) A='0'+A;
		int bln=B.size();
		for(int i=0;i<120-bln;i++) B='0'+B;
		int ans=getcnt(B)-getcnt(A);
		if(binary_search(palin.begin(),palin.end(),A)) ans++;
		printf("Case #%d: %d\n",datano+1,ans);
	}
	return 0;
}
