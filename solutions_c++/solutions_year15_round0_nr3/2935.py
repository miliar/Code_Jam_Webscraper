#include<bits/stdc++.h>
using namespace std;
class quaternion
{
public:
	int i,x,y,z;
	quaternion(int a, int b, int c, int d)
	{
		i=a;x=b;y=c;z=d;
	}
};
quaternion prod(quaternion p, int k)
{
	int a1 = p.i;
	int b1 = p.x;
	int c1 = p.y;
	int d1 = p.z;
	int a2 = 0;
	int b2 = 0;
	int c2 = 0;
	int d2 = 0;
	if(k==0)b2=1;
	if(k==1)c2=1;
	if(k==2)d2=1;
	quaternion res(0,0,0,0);
	res.i = a1*a2 - b1*b2 - c1*c2 - d1*d2;
	res.x = a1*b2 + b1*a2 + c1*d2 - d1*c2;
	res.y = a1*c2 - b1*d2 + c1*a2 + d1*b2;
	res.z = a1*d2 + b1*c2 - c1*b2 + d1*a2;
	return res;
}
bool eqq(quaternion a, quaternion b)
{
	return(a.i==b.i && a.x==b.x && a.y==b.y && a.z==b.z);
}
bool equal(quaternion x, int y)
{
	quaternion vx(0,1,0,0);
	quaternion vy(0,0,1,0);
	quaternion vz(0,0,0,1);
	quaternion id(-1,0,0,0);
	if(y==1)
		return eqq(x, vx);
	else if(y==2)
		return eqq(x, vy);
	else if(y==3)
		return eqq(x, vz);
	else if(y==0)
		return eqq(x, id);
	else
		return false;
}
int main()
{
	int t,i,j,p,l,k,x,curr;
	string s;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		curr=1;
		cin>>l>>x>>s;
		quaternion temp(1,0,0,0);
		quaternion tmp(1,0,0,0);
		vector<quaternion> arr(l*x, quaternion(0,0,0,0));
		for(j=0;j<l*x;j++)
		{
			p = j%l;
			if(s[p]=='i')
				k=0;
			else if(s[p]=='j')
				k=1;
			else if(s[p]=='k')
				k=2;
			//temp = prod(temp, k);
			arr[j] = tmp = prod(tmp,k);
		}
		curr = 0;
		vector<quaternion> v(3, quaternion(0,0,0,0));
		v[0].x=1;
		v[1].z=1;
		v[2].i=-1;
		for(j=0;j<l*x;j++)
		{
			if(eqq(v[curr],arr[j]))
				curr++;
		}
		if(curr == 3 && eqq(arr[l*x-1], v[2]))
		{
			cout<<"Case #"<<i<<": YES\n";
		}
		else
		{
			cout<<"Case #"<<i<<": NO\n";
		}
	}
	return 0;
}