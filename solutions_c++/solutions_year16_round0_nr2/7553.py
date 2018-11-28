#include<iostream>
#include<fstream>


using namespace std;


int len (char a[]);
int iscorrect (char a[]);
char reverse (char a);
int lastdash (char a[]);
int lastplus (char a[]);

int main()
{
cout<<"Enter file name";
string file;
cin>>file;

ifstream infile;
infile.open(file);

ofstream out;
out.open("output.txt");

int N;
infile>>N;

char a[110];
for(int i=0;i<N;i++){

	infile>>a;
	int n=0;

	while(!iscorrect(a)){
		if(a[0]=='-'){
			n++;
			int o=lastdash(a);
			for(int j=0;j<=lastdash(a)/2;j++)
				{
					char temp = a[j];

					a[j] = a[lastdash(a)-j];
					a[lastdash(a)-j]=temp;

				}
			for(int p=0;p<=o;p++){
				a[p]=reverse(a[p]);
			}
		}
		else if(a[0]=='+'){
			n++;
			int o=lastplus(a);
			for(int j=0;j<=lastplus(a)/2;j++)
				{
					char temp = a[j];

					a[j] = a[lastplus(a)-j];
					a[lastplus(a)-j]=temp;
				}
			for(int p=0;p<=o;p++){
				a[p]=reverse(a[p]);
			}

		}

	}
	out<<"Case #"<<i+1<<": "<<n<<endl;
	//work your logic  
}


}

char reverse (char a){
	if(a=='+')
		return '-';
	else
		return '+';
}

int lastdash (char a[]){

for(int i=len(a)-1;i>=0;i--)
	if(a[i]=='-')
		return i;

return -1;
}

int lastplus (char a[]){
	for(int i=lastdash(a);i>=0;i--)
		if(a[i]=='+')
			return i;
return -1;
}

int len (char a[]){

	int i;
	for(i=0;a[i]!='\0';i++);

	return i;


}

int iscorrect (char a[]){

	int b=1;
	for(int i=0;i<len(a);i++)
		if(a[i]=='-')
			b=0;

	return b;

}