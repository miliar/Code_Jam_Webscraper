# include <stdio.h>
# include <stdlib.h>
# include <cstdlib>
# include <iostream>
# include <cstdio>
# include <string>
# include <cstring>
# include <sstream>
# include <math.h>
# include <algorithm>
# include <set>
# include <map>
# include <vector>
# include <list>
# include <stack>
# include <queue>
# include <utility>

using namespace std;
////library for big int

class myint{
public:
	char sign;
	vector<char> no;
	int size;

	myint(){
		sign = '+';
		no.clear();
		no.push_back(0);
		size = 1;
	}

	void reset(long long int ini){
		if(ini == 0){
			sign = '+';
			no.clear();
			no.push_back(0);
			size = 1;
		}
		else{
			if(ini > 0){
				sign = '+';
			}
			else{
				sign = '-';
				ini *= -1;
			}
			no.clear();
			size = 0;
			char c;
			while(ini){
				c = (ini % 10);
				no.push_back(c);
				ini /= 10;
				size++;
			}
		}
	}

	myint(long long int ini){
		if(ini == 0){
			sign = '+';
			no.clear();
			no.push_back(0);
			size = 1;
		}
		else{
			if(ini > 0){
				sign = '+';
			}
			else{
				sign = '-';
				ini *= -1;
			}
			no.clear();
			size = 0;
			char c;
			while(ini){
				c = (ini % 10);
				no.push_back(c);
				ini /= 10;
				size++;
			}
		}
	}

	int mymodcmp(myint a){	// ret >0 means this > a
		if(size == 0)return a.size;
		if(a.size == 0)return size;
		if(size > a.size)return 1;
		if(a.size > size)return -1;
		int i = size;
		while(i--){
			if(no[i] == a.no[i]){
				continue;
			}
			else{
				return (no[i]-a.no[i]);
			}
		}
		return 0;
	}

	int mycmp(myint a){
		if(sign == '+'){
			if(a.sign == '+')
				return mymodcmp(a);
			else
				return 1;
		}
		if(a.sign == '-')
			return (a.mymodcmp(*this));
		else
			return -1;
	}

	void mysub(myint inp){			// destroys a
		myint a = inp;
		if(a.size == 0)return;
		if(size == 0){
			no = a.no;
			size = a.size;
			sign = a.sign;
			return;
		}
		if((sign ^ a.sign) != 0){
			a.sign ^= ('+')^('-');
			myadd(a);
			return;
		}
		int compared = mymodcmp(a);
		if(compared == 0){
			sign = '+';
			size = 1;
			no.clear();
			no.push_back(0);
			return;
		}
		vector <char> tmp_no;
		int tmp_size = 0,carrier;
		
		if(compared > 0){
			while((tmp_size < a.size)){		//---> (tmp_size < size)  is obvious here as (compared > 0)
				if(no[tmp_size] >= a.no[tmp_size]){
					tmp_no.push_back(no[tmp_size] - a.no[tmp_size]);
				}
				else{
					tmp_no.push_back(no[tmp_size] - a.no[tmp_size] + 10);
					carrier = tmp_size + 1;
					while((carrier < a.size)&&(no[carrier] <= a.no[carrier])){
						no[carrier] += 9;
						carrier++;
					}
					while(no[carrier] == 0){
						no[carrier] = 9;
						carrier++;
					}
					no[carrier]--;			//remove 1 as a carry if not 0 else search for such elem
				}

				tmp_size++;
			}
			while(tmp_size < size){
				tmp_no.push_back(no[tmp_size]);
				tmp_size++;
			}
		}
		else{
			sign ^= ('+')^('-');
			while((tmp_size < size)){		//---> (tmp_size < size)  is obvious here as (compared > 0)
				if(a.no[tmp_size] >= no[tmp_size]){
					tmp_no.push_back(a.no[tmp_size] - no[tmp_size]);
				}
				else{
					tmp_no.push_back(a.no[tmp_size] - no[tmp_size] + 10);
					carrier = tmp_size + 1;
					while((carrier < size)&&(a.no[carrier] <= no[carrier])){
						a.no[carrier] += 9;
						carrier++;
					}
					while(a.no[carrier] == 0){
						a.no[carrier] = 9;
						carrier++;
					}
					a.no[carrier]--;			//remove 1 as a carry if not 0 else search for such elem
				}

				tmp_size++;
			}
			while(tmp_size < a.size){
				tmp_no.push_back(a.no[tmp_size]);
				tmp_size++;
			}
		}
		no.clear();
		size = tmp_size;
		while(tmp_no[size-1] == 0)tmp_size--;
		carrier = 0;
		while(carrier < tmp_size){
			no.push_back(tmp_no[carrier]);
			carrier++;
		}
		size = tmp_size;
	}

	void myadd(myint a){
		if(a.size == 0)return;
		if(size == 0){
			no = a.no;
			size = a.size;
			sign = a.sign;
			return;
		}
		if((sign ^ a.sign) != 0){
			char sn = sign;
			a.sign ^= ('+')^('-');
			mysub(a);
			return;
		}
		vector <char> tmp_no;
		int tmp_size = 0;
		long long int carry = 0;
		while((tmp_size < size)&&(tmp_size < a.size)){
			carry += no[tmp_size] + a.no[tmp_size];
			tmp_no.push_back(carry%10);
			carry/=10;
			tmp_size++;
		}
		if(size > a.size){
			while(tmp_size < size){
				carry += no[tmp_size];
				tmp_no.push_back(carry%10);
				carry /= 10;
				tmp_size++;
			}
			while(carry){
				tmp_no.push_back(carry%10);
				carry /= 10;
				tmp_size++;
			}
		}
		else{
			while(tmp_size < a.size){
				carry += a.no[tmp_size];
				tmp_no.push_back(carry%10);
				carry /= 10;
				tmp_size++;
			}
			while(carry){
				tmp_no.push_back(carry%10);
				carry /= 10;
				tmp_size++;
			}
		}
		size = tmp_size;
		no.clear();
		no = tmp_no;
	}

	void myprod(long long int mul){
		if(mul == 0){
			no.clear();
			no.push_back(0);
			size = 1;
			sign = '+';
			return;
		}
		if(mul < 0){
			sign ^= ('+')^('-');
			mul *= -1;
		}
		if(mul == 1)
			return;
		long long int carry = 0;
		int i = 0;
		while(i < size){
			carry += (no[i])*mul;
			no[i] = (carry % 10);
			carry /= 10;
			i++;
		}
		while(carry){
			no.push_back((carry % 10));
			carry /= 10;
			size++;
		}
	}
};


int main(void){
	unsigned long long int case_no,i,y1,y,y2,t,r,j,k,l,m,n;
	scanf("%lld\n",&case_no);
	for(i = 1 ; i <= case_no ; i++){
		scanf("%lld %lld\n",&r,&t);
		y = y1 = 1; y2 = 1000000000;
		while(y2-y1>1){
			m = y1+(y2-y1)/2;
			myint a = myint(m),b = myint(t);
			a.myprod(2*m+2*r-1);
			if(a.mycmp(t) <= 0){
				if(m > y) y = m;
				y1 = m;
			}
			else{
				y2 = m;
			}
		}
		printf("Case #%lld: %lld\n",i,y);
	}



	return 0;
}
