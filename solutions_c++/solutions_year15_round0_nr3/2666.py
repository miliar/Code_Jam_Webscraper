#include <iostream>
#include <algorithm>
#include <iomanip>
#include <climits>
#include <cstring>
int num[10010],value[10010],fl;
char str[10010];
void prod(int,int,int[5][5]);
void search(int,int,int[5][5]);
void evaluatek(int,int,int[5][5]);
using namespace std;
int mat[5][5];

int main()
{
int T,z,l,x,w,r,p1,p2,p3,p,i,j,k,maxi;
mat[1][1]=1;
mat[1][2]=2;
mat[1][3]=3;
mat[1][4]=4;
mat[2][1]=2;
mat[2][2]=-1;
mat[2][3]=4;
mat[2][4]=-3;
mat[3][1]=3;
mat[3][2]=-4;
mat[3][3]=-1;
mat[3][4]=2;
mat[4][1]=4;
mat[4][2]=3;
mat[4][3]=-2;
mat[4][4]=-1;

freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
cin >> T;
for(z=1;z<=T;z++)
{
cin >> l >> x;
cin >> str;
fl=0;
for(p=0;p<l;p++){
	if(str[p]=='i')
	num[p+1]=2;
	else if(str[p]=='j')
	num[p+1]=3;
	else if(str[p]=='k')
	num[p+1]=4;
}
p++;
for(w=1;w<x;w++){
for(r=1;r<=l;r++){
	num[p]=num[r];
	p++;
}	
}

//cout << "here"<< endl;

maxi=l*x;
evaluatek(maxi,1,mat);
prod(1,maxi,mat);
//for(i=1;i<=maxi;i++)
//cout << value[i] << " ";
//cout << endl;
//cout << "confirmed"<< endl;
//fl=1;
/*
for(i=3;i<=maxi && val[i]==4 && fl;i++){
		for(q=1;q<i-1;q++){
		}			
			p1=prod(1,q,mat);
			
			p2=prod(q+1,i-1,mat);
			
		//	if (i==3 && j==6)
		//	cout << p1 << " " << p2 << " " << p3 << endl;
			if(p1==2 && p2==3){
				fl=0;
			}
	
	
}*/
cout<< "Case #" << z <<": ";
if(fl==0)
cout << "NO" << endl;
else
cout << "YES" << endl;
}

return 0;
}

void prod(int s,int e,int mat[5][5])
{
//	cout <<"prod"<<endl;
int cur,j,temp;
cur=num[s];

if(s<=e-2 && cur==2){
//cout << cur << " " << s << endl;
search(s+1,e,mat);
}
for(j=s;j<e;j++){
	temp=num[j+1];
	if(temp<0 && cur>0)
	cur=-mat[cur][-temp];
	else if(temp>0 && cur<0)
	cur=-mat[-cur][temp];
	else if(temp <0 && cur <0)
	cur=mat[-cur][-temp];
	else
	cur=mat[cur][temp];
	
	if(j<=e-3 && cur==2){
//		cout << cur << " " << j+1 <<endl;
		search(j+2,e,mat);
	}
  }	
 	
}

void search(int s,int e,int mat[5][5])
{
//	cout << "search" <<endl;
int cur,j,temp;
cur=num[s];

if(s<=e-1 && cur==3)
{
//	cout << cur << " " << s <<  value[s+1]<<endl;
	if(value[s+1]==4)
	   fl=1;
//	   cout << "fl " << fl << endl;
	   
}

for(j=s;j<e;j++){
	temp=num[j+1];
	if(temp<0 && cur>0)
	cur=-mat[cur][-temp];
	else if(temp>0 && cur<0)
	cur=-mat[-cur][temp];
	else if(temp <0 && cur <0)
	cur=mat[-cur][-temp];
	else
	cur=mat[cur][temp];

	if(j<=e-2 && cur==3){
//		cout << cur << " " << j+1 << " "<< value[j+2]<<endl;
		if(value[j+2]==4)
		  fl=1;
//		  cout << "fl " << fl << endl;
	}
  }		
	
}

void evaluatek(int big,int sm,int mat[5][5])
{
int cur,temp,i;
value[big]=num[big];
cur=num[big];
	
for(i=big-1;i>=sm;i--)
{
	temp=num[i];
	if(temp<0 && cur>0)
	cur=-mat[-temp][cur];
	else if(temp>0 && cur<0)
	cur=-mat[temp][-cur];
	else if(temp <0 && cur <0)
	cur=mat[-temp][-cur];
	else
	cur=mat[temp][cur];
	value[i]=cur;
}	
	
}
