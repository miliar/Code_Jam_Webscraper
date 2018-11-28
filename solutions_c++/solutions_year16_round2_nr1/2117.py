#include<bits/stdc++.h>


#define pb push_back
#define mp make_pair
#define f first
#define s second
#define ll long long int
#define MOD 1000000007

using namespace std; 

int A[26];
string S;
int ans[10];

int func1(char ch)
{
	return A[(int)(ch-'A')];
}

void fn2(char ch,int a)
{
	A[(int)(ch-'A')]-=a;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		for(i=0;i<26;i++)
			A[i]=0;
		cin>>S;
		int l=S.length();
		for(i=0;i<l;i++)
			A[(int)(S[i]-'A')]++;
		int temp=func1('Z');
		ans[0]=temp;
		fn2('Z',temp);fn2('E',temp);fn2('R',temp);fn2('O',temp);
		temp=func1('W');
		ans[2]=temp;
		fn2('T',temp);fn2('W',temp);fn2('O',temp);
		temp=func1('X');
		ans[6]=temp;
		fn2('S',temp);fn2('I',temp);fn2('X',temp);
		temp=func1('U');
		ans[4]=temp;
		fn2('F',temp);fn2('O',temp);fn2('U',temp);fn2('R',temp);
		temp=func1('G');
		ans[8]=temp;
		fn2('E',temp);fn2('I',temp);fn2('G',temp);fn2('H',temp);fn2('T',temp);
		temp=func1('S');
		ans[7]=temp;
		fn2('S',temp);fn2('E',temp);fn2('V',temp);fn2('E',temp);fn2('N',temp);
		temp=func1('F');
		ans[5]=temp;
		fn2('F',temp);fn2('I',temp);fn2('V',temp);fn2('E',temp);
		temp=func1('I');
		ans[9]=temp;
		fn2('N',temp);fn2('I',temp);fn2('N',temp);fn2('E',temp);
		temp=func1('R');
		ans[3]=temp;
		fn2('T',temp);fn2('H',temp);fn2('R',temp);fn2('E',temp);fn2('E',temp);
		temp=func1('N');
		ans[1]=temp;
		fn2('O',temp);fn2('N',temp);fn2('E',temp);
		for(i=0;i<26;i++)
			assert(A[i]==0);
		printf("Case #%d: ",k);
		for(i=0;i<10;i++)
			while(ans[i]--)
				cout<<i;
		cout<<endl;
	}
	return 0;
}
