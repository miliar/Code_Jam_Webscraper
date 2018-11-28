#include<fstream.h>
#include<string.h>
#include<math.h>
ifstream in("C.in");
ofstream out("output.txt");
int Test,Ans;
int A,B,Cnt;
char Num[102];
void convertInt(int number)
{
	Cnt=0;
    if (number==0){
        Cnt=1;
		Num[0]=0;
		return;
	}
    while (number>0)
    {
        Num[Cnt]=char((number%10)+"0");
		Cnt++;
        number/=10;
    }
}

int Palin(int node)
{
	int i;
	convertInt(node);
	for(i=0;i<Cnt/2;i++){
		if(Num[i]!=Num[Cnt-i-1])return 0;
	}
	convertInt(node*node);
	for(i=0;i<Cnt/2;i++){
		if(Num[i]!=Num[Cnt-i-1])return 0;
	}
	return 1;
}
int main()
{
	int i,j;
	in>>Test;
	for(i=0;i<Test;i++){
		in>>A>>B;
		if(double(sqrt(A))>double(int(sqrt(A)))){
			A=int(sqrt(A))+1;
		}
		else{
			A=int(sqrt(A));
		}
		B=int(sqrt(B));
		Ans=0;
		for(j=A;j<=B;j++){
			if(Palin(j)==1){
				Ans++;
			}
		}
		out<<"Case #"<<i+1<<": "<<Ans<<"\n";
	}
	return 0;
}