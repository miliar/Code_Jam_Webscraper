#include<iostream>
#include<vector>
using namespace std;
long long a,b;
vector<long long> result;
bool is_palin(long long num)
{
	int ch[100];
	int len=0;
	while(num>0){
		ch[len]=num%10;
		num/=10;
		len++;
	}
	for(int i=0;i<=len/2;i++){
		if(ch[i]!=ch[len-i-1])
			return false;
	}
	return true;
}
long long pow(long long base, int n)
{
	long long result=1;
	for(int i=0;i<n;i++){
		result*=base;
	}
	return result;
}
long long rev_num(long long num)
{
	int res=0;
	while(num>0){
		res*=10;
		res+=num%10;
		num/=10;
	}
	return res;
}
void gen_pal(int n)
{
	int half=n/2;
	int mod=n%2;
	
	long long end=pow(10,half+mod)-1;
	long long start=(end+1)/10;
	
	for(int i=start;i<=end;i++){
		long long pal_num=i*pow(10,half)+rev_num(mod?i/10:i);
		long long pal_sqr=pal_num*pal_num;
		if(pal_sqr>100000000000000)
			break;
		if(is_palin(pal_sqr)){
			result.push_back(pal_sqr);
			//cout<<pal_sqr<<endl;
		}
	}
}
int main(int argc, char **argv)
{
	result.push_back(1);
	result.push_back(4);
	result.push_back(9);
	for(int i=2;i<=8;i++){
		gen_pal(i);
	}
	int total_size=result.size();
	//cout<<result.size()<<endl;
	int tc=0;
	cin>>tc;
	for (int c = 1; c <= tc; ++c)
	{
			cin>>a>>b;
			int ans=0;
			for(int i=0;i<total_size;i++){
				if(result[i]>b)
					break;
				if(result[i]>=a)
					ans++;
			}
			cout<<"Case #"<<c<<": "<<ans<<endl;
	}
	return 0;
}
