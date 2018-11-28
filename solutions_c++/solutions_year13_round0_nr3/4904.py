#include<iostream>
#include<cmath>

using namespace std;

int GetPalindrome(int pal)
{
  int next = 0;
  int pal2 = pal;

  while (pal2 != 0)
  {
    next = (next * 10) + (pal2 % 10);
    pal2 /= 10;
  }

  if (pal == next)
  {
    return 1;
  }
  else
  {
    return 0;
  }
}

void main(){
	int T,A,B,tmp,num;
	double root;
	
	cin>>T;
	for(int i=1;i<=T;i++){
		num=0;
		scanf_s("%d %d",&A,&B);
		for(int c=A;c<=B;c++){
			if(GetPalindrome(c)){
				root  = sqrt((double) c);
				if(floor(root)==root){
					tmp = (int) root;
					if(GetPalindrome(tmp)) num++;
				}
			}
		}
		cout << "Case #"<< i <<": " << num << endl;
	}
}