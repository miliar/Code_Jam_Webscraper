/*Odd bases -> set an even number of bit => divisible by 2

4,8,10 -> Set Nbits set should be a multiple of 3 => divisible by 3

6 -> Nbits set multiple of 5

2*3*5

28 30
*/
#include <bits/stdc++.h>
using namespace std;

#define  BX_(x)         ((x) - (((x)>>1)&0x77777777)                    \
                             - (((x)>>2)&0x33333333)                    \
                             - (((x)>>3)&0x11111111))


#define BITCOUNT(x)     (((BX_(x)+(BX_(x)>>4)) & 0x0F0F0F0F) % 255)

vector< unsigned int > ans;

int main(){
	int c;cin>>c;
	int N,J;cin>>N>>J;
	register unsigned int x=0,limit=0;
	x |= ((unsigned int)1<<(N-1));
	for(int i=0;i<N;i++) limit |= ((unsigned int)1<<(i));
	x += 1;
	for(;x<limit;x+=2){
		if(BITCOUNT(x)%3 == 0 && BITCOUNT(x)%2 == 0 && x%3 == 0){
			ans.push_back(x);
		}
		end:;
		if(ans.size() > J) break;
	}
	cout<<"Case #1:"<<endl;
	for(int i=0;i<J;i++){
		bitset<32> x(ans[i]);
		cout<<x<<" 3 2 3 2 7 2 3 2 3"<<endl;
	}
	return 0;
}
			
	

