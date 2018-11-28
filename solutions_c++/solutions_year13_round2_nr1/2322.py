#include <iostream>
#include <list>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>

#define ASCII_SPACE 32
#define ASCII_NEWLINE 10


using namespace std;




#define PRINT_TOKEN(token)\
	do{\
		cout<<#token<<" is "<<token<<endl; \
	}while(0)


#define READ(arg)\
	do{\
		long long arg;\
		cin>>arg;\
	}while(0)

//#define PRINT_ARR()
typedef long long ll;

ll A,N;
ll m[100];
ll eval_add_times(ll base, ll target, ll* obase)
{
	ll times = 0;
	ll factor = base - 1;

	if(factor == 0) return -1;
	while(base <= target){
		
		base = base + factor;
		factor += factor;

		times++;
	}
	*obase = base;
	return times;
}

ll solve()
{
	sort(m,m+N);

	for(int i=0;i<N;i++){
		//cout<<","<<m[i];
	}
	//cout<<endl;

	ll op_times=0;
	ll mSize=A;
	for(int i=0;i<N;i++){
		if(mSize > m[i]){
			mSize += m[i];
			//cout<<"op_times:"<<op_times<<",mote:"<<mSize<<endl;
		}else{
			ll temp_mSize;
			int add_times = eval_add_times(mSize, m[i], &temp_mSize);
			int remove_times = N - i;

			if(add_times != -1 &&  add_times < remove_times){
				mSize = temp_mSize;
				op_times += add_times;
				i--;
				//cout<<"Add:"<<mSize<<",times="<<add_times<<endl;
				//cout<<"op_times:"<<op_times<<",mote:"<<mSize<<endl;
			}else{
				op_times += remove_times;
				//cout<<"Remove:"<<i<<",times="<<remove_times<<endl;
				//cout<<"op_times:"<<op_times<<endl;
				return op_times;
			}
		}
	}

	//cout<<"op_times:"<<op_times<<endl;
	return op_times;
}

int main()
{
	long long T;

	cin>>T;

	for(long long i=0;i<T;i++){
		cin >> A >>N;
		//cout<<"A:"<<A<<",N:"<<N<<endl;
		long long result=0 ;
		for(int a=0;a<N;a++){
			cin >> m[a];
		}
		result = solve();
		cout<<"Case "<<"#"<<i+1<<": "<<result;
		cout<<endl;

	}
	return 0;
}


