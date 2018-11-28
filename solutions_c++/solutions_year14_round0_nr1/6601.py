#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main() {
	int cards[17];
	fstream in22("A-small-attempt0.in");
	fstream out22("a-small.out",ios::trunc | ios::out);
	string ttt;
    int t, answer, k, i, n, number, ncards;
    in22>>t;
    cout<<t<<' '<<endl;
     for (i=1;i<=t;++i){
       
       for (k=1;k<=16;++k)cards[k]=0;
       
       in22>>answer;
       for (k=1;k<answer;++k)
         for (n=1;n<=4;++n) in22>>number;
         for (n=1;n<=4;++n){in22>>number; cards[number]++; cout << number << " ";} cout<<endl;
       for (k=answer+1;k<=4;++k)
         for (n=1;n<=4;++n) in22>>number;
         
       in22>>answer;
       for (k=1;k<answer;++k)
         for (n=1;n<=4;++n) in22>>number;
         for (n=1;n<=4;++n){in22>>number; cards[number]++;cout << number << " ";} cout<<endl;
       for (k=answer+1;k<=4;++k)
         for (n=1;n<=4;++n) in22>>number;
       
       ncards=0;  
       for (k=1;k<=16;++k)if (cards[k]==2){++ncards; answer=k;}
       
       if (ncards==0) out22<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
       if (ncards==1) out22<<"Case #"<<i<<": "<<answer<<endl;
       if (ncards>1)  out22<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
    }
      cin.ignore();
      in22.close();
      out22.close();
    return 0;
}
