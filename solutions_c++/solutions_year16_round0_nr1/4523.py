#include<iostream>
using namespace std;

bool alltrue(bool *arr)
{
	for(int i=0;i<10;i++)
		if(arr[i]==0)
			return 0;

	return 1;
}
uint64_t getNum(uint64_t n)
{
	bool arr[10]={0};
	int i=1;
	int num=n;
	while(1)
	{
		//cout<<n<<endl;
		int tmp=n;
		while(tmp)
		{
			int dig = tmp%10;
			arr[dig]=1;
			tmp=tmp/10;
		}
		if(alltrue(arr))
			break;
		n=(i+1)*num;
		i++;
		//cout<<n<<endl;
	}
	return n;
}
int main()
{
	int t;
	uint64_t n;
    cin>>t;
    int cnt=1;
    while(t--)
    {
    	cin>>n;
    	if(n==0)
    		cout<<"Case #"<< cnt++<<": INSOMNIA"<<endl;
    	else
    	{
    		uint64_t num= getNum(n);
    		cout<<"Case #"<< cnt++<<": "<<num<<endl;
    	}
    }

}