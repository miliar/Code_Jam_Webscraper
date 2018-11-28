int N;
int Count[26];

inline bool check(){
	int i,sum=0;

	for(i=0;i<N;++i)
		sum+=Count[i];

	for(i=0;i<N;++i)
		if(Count[i]>(sum>>1))
			return false;
	return true;
}

inline bool empty(){
	int i;
	for(i=0;i<N && Count[i]==0;++i);
	if(i==N)
		return true;
	return false;
}

inline void Do(){
cin>>N;

int i;
for(i=0;i<N;++i)
	cin>>Count[i];

int A,B;
while(!empty()){
	for(A=0;A<N;++A){
		for(B=A+1;B<N;++B){
			--Count[A];
			--Count[B];
			if(check())
				cout<<(char)('A'+A)<<(char)('A'+B)<<' ';
			else{
				++Count[B];
				if(check())
					cout<<(char)('A'+A)<<' ';
				else
					++Count[A];
			}
		}
	}
}

}
