#include <fstream>
#include <math.h>
#include <conio.h>
using namespace std;
ifstream fin("in.txt");
ofstream fout("out.txt");
bool palin(int num){
	
	int r,sum=0,temp;
	bool flag;
    for(temp=num;num!=0;num=num/10){
         r=num%10;
         sum=sum*10+r;
    }
    if(temp==sum){ 
		flag = true;
        return flag;
    }
    else{
		flag = false;
		return flag;
	}
}

int main(){
	int N;
	fin>>N;
	long long A,B;
	int n = N;
	int ctr = 0;
	long long pal[N];
	while(n > 0){
	fin>>A>>B;
	long long s;
	bool flag1, flag2;
	int ct = 0;
	for(long long i=1; i <= floor(sqrt(B)); i++)
    {
		s = i * i;
		flag1 = palin(i);
		flag2 = palin(s);
		if(flag1 == true && flag2 == true && s >= A){ct++;}
	}
	pal[ctr] = ct; ctr++;
	n--;
}
for(int j = 0; j < N; j++){fout<<"Case #"<<j+1<<": "<<pal[j]<<'\n';}
getch();
return 0;
}
