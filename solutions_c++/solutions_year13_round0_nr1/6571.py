#include<iostream>
#include<cstdio>
#include<algorithm>
#include<numeric>
#include<cstring>
#include<set>
#include<utility>
#include<vector>
using namespace std;
//int a[101],b[101];
int main()
{
	int t,ctoc,ctxr,ctxc,ctor,flag;
	vector <string> v;
	string s1,s2,s3,s4;
	cin >>t;int k=1;
	while(k<=t)
	{
		flag =0;
		v.clear();
		s1.clear();
		s2.clear();
		s3.clear();
		s4.clear();
//		s.clear();
		cin >> s1;
		v.push_back(s1);
		cin >> s2;
		v.push_back(s2);
		cin >> s3;
		v.push_back(s3);
		cin >> s4;
		v.push_back(s4);
		for(int i=0; i<4 ;i++)
		{
			ctxr =0 ;
			for(int j =0 ; j <4 ;j++)
			{
				if(v[i][j]=='X' || v[i][j] == 'T')
					ctxr++;
			}
			if(ctxr == 4) {flag=1;break;}
		}
		//cout <<"ctxr = "<<ctxr <<endl;
		//cout <<"flag = "<<flag <<endl;
		for(int i=0; i<4 ;i++)
		{
			ctxc =0 ;
			for(int j =0 ; j <4 ;j++)
			{
				if(v[j][i]=='X' || v[j][i] == 'T')
					ctxc++;
			}
			if(ctxc == 4){flag=1;break;}
		}
		//cout <<"ctxc = "<<ctxc <<endl;
		for(int i=0; i<4 ;i++)
		{
			ctor =0 ;
			for(int j =0 ; j <4 ;j++)
			{
				if(v[i][j]=='O' || v[i][j] == 'T')
					ctor++;
			}
			if(ctor == 4) {flag=2;break;}
		}
		for(int i=0; i<4 ;i++)
		{
			ctoc =0 ;
			for(int j =0 ; j <4 ;j++)
			{
				if(v[j][i]=='O' || v[j][i] == 'T')
					ctoc++;
			}
			if(ctoc == 4){flag=2;break;}
		}
		if ((v[0][0] == 'T' || v[0][0] == 'X') && (v[1][1] == 'T' || v[1][1] == 'X') && (v[2][2] == 'T' || v[2][2] == 'X') && (v[3][3] == 'T' || v[3][3] == 'X') ) flag =1;
		if ((v[0][3] == 'T' || v[0][3] == 'X') && (v[1][2] == 'T' || v[1][2] == 'X') && (v[2][1] == 'T' || v[2][1] == 'X') && (v[3][0] == 'T' || v[3][0] == 'X') ) flag =1;
		if ((v[0][0] == 'T' || v[0][0] == 'O') && (v[1][1] == 'T' || v[1][1] == 'O') && (v[2][2] == 'T' || v[2][2] == 'O') && (v[3][3] == 'T' || v[3][3] == 'O') ) flag =2;
		if ((v[0][3] == 'T' || v[0][3] == 'O') && (v[1][2] == 'T' || v[1][2] == 'O') && (v[2][1] == 'T' || v[2][1] == 'O') && (v[3][0] == 'T' || v[3][0] == 'O') ) flag =2;
//		cout <<"flag = "<<flag<<endl;
		if(flag !=1 && flag !=2){
		for(int i=0; i< 4;i++)
		{
			for(int j=0; j<4 ;j++)
			{
				if(v[i][j] == '.' )
				{
					flag =3;break;
				}
			}
		}
		}
	//	cout << "flag = " <<flag<<endl;
		if(flag ==1)
			cout <<"Case #"<<k<<": X won"<<endl;
		else if(flag ==2)
			cout <<"Case #"<<k<<": O won"<<endl;
		else if(flag ==3)
			cout <<"Case #"<<k<<": Game has not completed"<<endl;
		else 
			cout <<"Case #"<<k<<": Draw"<<endl;
		k++;flag=0;
	}
return 0;
}
	
