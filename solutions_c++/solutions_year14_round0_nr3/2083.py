#include<iostream>
using namespace std;
int main(){
  int ttt;
  cin >> ttt;
  for(int tt=0; tt<ttt; ++tt){
    printf("Case #%d:\n", tt+1);
    int r, c, m;
    cin >> r >> c >> m;
    if(r==1 && c==1 && m==0)
      printf("c\n");
    if(r==1 && c==2 && m==0)
      printf("c.\n");
    if(r==1 && c==2 && m==1)
      printf("*c\n");
    if(r==1 && c==3 && m==0)
      printf("c..\n");
    if(r==1 && c==3 && m==1)
      printf("*.c\n");
    if(r==1 && c==3 && m==2)
      printf("**c\n");
    if(r==1 && c==4 && m==0)
      printf("c...\n");
    if(r==1 && c==4 && m==1)
      printf("*.c.\n");
    if(r==1 && c==4 && m==2)
      printf("**.c\n");
    if(r==1 && c==4 && m==3)
      printf("***c\n");
    if(r==1 && c==5 && m==0)
      printf("c....\n");
    if(r==1 && c==5 && m==1)
      printf("*.c..\n");
    if(r==1 && c==5 && m==2)
      printf("**.c.\n");
    if(r==1 && c==5 && m==3)
      printf("***.c\n");
    if(r==1 && c==5 && m==4)
      printf("****c\n");
    if(r==2 && c==1 && m==0)
      printf("c\n.\n");
    if(r==2 && c==1 && m==1)
      printf("*\nc\n");
    if(r==2 && c==2 && m==0)
      printf("c.\n..\n");
    if(r==2 && c==2 && m==1)
      printf("Impossible\n");
    if(r==2 && c==2 && m==2)
      printf("Impossible\n");
    if(r==2 && c==2 && m==3)
      printf("**\n*c\n");
    if(r==2 && c==3 && m==0)
      printf("c..\n...\n");
    if(r==2 && c==3 && m==1)
      printf("Impossible\n");
    if(r==2 && c==3 && m==2)
      printf("*.c\n*..\n");
    if(r==2 && c==3 && m==3)
      printf("Impossible\n");
    if(r==2 && c==3 && m==4)
      printf("Impossible\n");
    if(r==2 && c==3 && m==5)
      printf("***\n**c\n");
    if(r==2 && c==4 && m==0)
      printf("c...\n....\n");
    if(r==2 && c==4 && m==1)
      printf("Impossible\n");
    if(r==2 && c==4 && m==2)
      printf("*.c.\n*...\n");
    if(r==2 && c==4 && m==3)
      printf("Impossible\n");
    if(r==2 && c==4 && m==4)
      printf("**.c\n**..\n");
    if(r==2 && c==4 && m==5)
      printf("Impossible\n");
    if(r==2 && c==4 && m==6)
      printf("Impossible\n");
    if(r==2 && c==4 && m==7)
      printf("****\n***c\n");
    if(r==2 && c==5 && m==0)
      printf("c....\n.....\n");
    if(r==2 && c==5 && m==1)
      printf("Impossible\n");
    if(r==2 && c==5 && m==2)
      printf("*.c..\n*....\n");
    if(r==2 && c==5 && m==3)
      printf("Impossible\n");
    if(r==2 && c==5 && m==4)
      printf("**.c.\n**...\n");
    if(r==2 && c==5 && m==5)
      printf("Impossible\n");
    if(r==2 && c==5 && m==6)
      printf("***.c\n***..\n");
    if(r==2 && c==5 && m==7)
      printf("Impossible\n");
    if(r==2 && c==5 && m==8)
      printf("Impossible\n");
    if(r==2 && c==5 && m==9)
      printf("*****\n****c\n");
    if(r==3 && c==1 && m==0)
      printf("c\n.\n.\n");
    if(r==3 && c==1 && m==1)
      printf("*\n.\nc\n");
    if(r==3 && c==1 && m==2)
      printf("*\n*\nc\n");
    if(r==3 && c==2 && m==0)
      printf("c.\n..\n..\n");
    if(r==3 && c==2 && m==1)
      printf("Impossible\n");
    if(r==3 && c==2 && m==2)
      printf("**\n..\nc.\n");
    if(r==3 && c==2 && m==3)
      printf("Impossible\n");
    if(r==3 && c==2 && m==4)
      printf("Impossible\n");
    if(r==3 && c==2 && m==5)
      printf("**\n**\n*c\n");
    if(r==3 && c==3 && m==0)
      printf("c..\n...\n...\n");
    if(r==3 && c==3 && m==1)
      printf("*.c\n...\n...\n");
    if(r==3 && c==3 && m==2)
      printf("Impossible\n");
    if(r==3 && c==3 && m==3)
      printf("***\n...\nc..\n");
    if(r==3 && c==3 && m==4)
      printf("Impossible\n");
    if(r==3 && c==3 && m==5)
      printf("***\n*..\n*.c\n");
    if(r==3 && c==3 && m==6)
      printf("Impossible\n");
    if(r==3 && c==3 && m==7)
      printf("Impossible\n");
    if(r==3 && c==3 && m==8)
      printf("***\n***\n**c\n");
    if(r==3 && c==4 && m==0)
      printf("c...\n....\n....\n");
    if(r==3 && c==4 && m==1)
      printf("*.c.\n....\n....\n");
    if(r==3 && c==4 && m==2)
      printf("**.c\n....\n....\n");
    if(r==3 && c==4 && m==3)
      printf("*.c.\n*...\n*...\n");
    if(r==3 && c==4 && m==4)
      printf("****\n....\nc...\n");
    if(r==3 && c==4 && m==5)
      printf("Impossible\n");
    if(r==3 && c==4 && m==6)
      printf("****\n*...\n*.c.\n");
    if(r==3 && c==4 && m==7)
      printf("Impossible\n");
    if(r==3 && c==4 && m==8)
      printf("****\n**..\n**.c\n");
    if(r==3 && c==4 && m==9)
      printf("Impossible\n");
    if(r==3 && c==4 && m==10)
      printf("Impossible\n");
    if(r==3 && c==4 && m==11)
      printf("****\n****\n***c\n");
    if(r==3 && c==5 && m==0)
      printf("c....\n.....\n.....\n");
    if(r==3 && c==5 && m==1)
      printf("*.c..\n.....\n.....\n");
    if(r==3 && c==5 && m==2)
      printf("**.c.\n.....\n.....\n");
    if(r==3 && c==5 && m==3)
      printf("***.c\n.....\n.....\n");
    if(r==3 && c==5 && m==4)
      printf("**.c.\n*....\n*....\n");
    if(r==3 && c==5 && m==5)
      printf("*****\n.....\nc....\n");
    if(r==3 && c==5 && m==6)
      printf("**.c.\n**...\n**...\n");
    if(r==3 && c==5 && m==7)
      printf("*****\n*....\n*.c..\n");
    if(r==3 && c==5 && m==8)
      printf("Impossible\n");
    if(r==3 && c==5 && m==9)
      printf("*****\n**...\n**.c.\n");
    if(r==3 && c==5 && m==10)
      printf("Impossible\n");
    if(r==3 && c==5 && m==11)
      printf("*****\n***..\n***.c\n");
    if(r==3 && c==5 && m==12)
      printf("Impossible\n");
    if(r==3 && c==5 && m==13)
      printf("Impossible\n");
    if(r==3 && c==5 && m==14)
      printf("*****\n*****\n****c\n");
    if(r==4 && c==1 && m==0)
      printf("c\n.\n.\n.\n");
    if(r==4 && c==1 && m==1)
      printf("*\n.\nc\n.\n");
    if(r==4 && c==1 && m==2)
      printf("*\n*\n.\nc\n");
    if(r==4 && c==1 && m==3)
      printf("*\n*\n*\nc\n");
    if(r==4 && c==2 && m==0)
      printf("c.\n..\n..\n..\n");
    if(r==4 && c==2 && m==1)
      printf("Impossible\n");
    if(r==4 && c==2 && m==2)
      printf("**\n..\nc.\n..\n");
    if(r==4 && c==2 && m==3)
      printf("Impossible\n");
    if(r==4 && c==2 && m==4)
      printf("**\n**\n..\nc.\n");
    if(r==4 && c==2 && m==5)
      printf("Impossible\n");
    if(r==4 && c==2 && m==6)
      printf("Impossible\n");
    if(r==4 && c==2 && m==7)
      printf("**\n**\n**\n*c\n");
    if(r==4 && c==3 && m==0)
      printf("c..\n...\n...\n...\n");
    if(r==4 && c==3 && m==1)
      printf("*.c\n...\n...\n...\n");
    if(r==4 && c==3 && m==2)
      printf("*.c\n*..\n...\n...\n");
    if(r==4 && c==3 && m==3)
      printf("***\n...\nc..\n...\n");
    if(r==4 && c==3 && m==4)
      printf("***\n*..\n..c\n...\n");
    if(r==4 && c==3 && m==5)
      printf("Impossible\n");
    if(r==4 && c==3 && m==6)
      printf("***\n***\n...\nc..\n");
    if(r==4 && c==3 && m==7)
      printf("Impossible\n");
    if(r==4 && c==3 && m==8)
      printf("***\n***\n*..\n*.c\n");
    if(r==4 && c==3 && m==9)
      printf("Impossible\n");
    if(r==4 && c==3 && m==10)
      printf("Impossible\n");
    if(r==4 && c==3 && m==11)
      printf("***\n***\n***\n**c\n");
    if(r==4 && c==4 && m==0)
      printf("c...\n....\n....\n....\n");
    if(r==4 && c==4 && m==1)
      printf("*.c.\n....\n....\n....\n");
    if(r==4 && c==4 && m==2)
      printf("**.c\n....\n....\n....\n");
    if(r==4 && c==4 && m==3)
      printf("**.c\n*...\n....\n....\n");
    if(r==4 && c==4 && m==4)
      printf("****\n....\nc...\n....\n");
    if(r==4 && c==4 && m==5)
      printf("****\n*...\n..c.\n....\n");
    if(r==4 && c==4 && m==6)
      printf("****\n**..\n...c\n....\n");
    if(r==4 && c==4 && m==7)
      printf("****\n*...\n*.c.\n*...\n");
    if(r==4 && c==4 && m==8)
      printf("****\n****\n....\nc...\n");
    if(r==4 && c==4 && m==9)
      printf("Impossible\n");
    if(r==4 && c==4 && m==10)
      printf("****\n****\n*...\n*.c.\n");
    if(r==4 && c==4 && m==11)
      printf("Impossible\n");
    if(r==4 && c==4 && m==12)
      printf("****\n****\n**..\n**.c\n");
    if(r==4 && c==4 && m==13)
      printf("Impossible\n");
    if(r==4 && c==4 && m==14)
      printf("Impossible\n");
    if(r==4 && c==4 && m==15)
      printf("****\n****\n****\n***c\n");
    if(r==4 && c==5 && m==0)
      printf("c....\n.....\n.....\n.....\n");
    if(r==4 && c==5 && m==1)
      printf("*.c..\n.....\n.....\n.....\n");
    if(r==4 && c==5 && m==2)
      printf("**.c.\n.....\n.....\n.....\n");
    if(r==4 && c==5 && m==3)
      printf("***.c\n.....\n.....\n.....\n");
    if(r==4 && c==5 && m==4)
      printf("***.c\n*....\n.....\n.....\n");
    if(r==4 && c==5 && m==5)
      printf("*****\n.....\nc....\n.....\n");
    if(r==4 && c==5 && m==6)
      printf("*****\n*....\n..c..\n.....\n");
    if(r==4 && c==5 && m==7)
      printf("*****\n**...\n...c.\n.....\n");
    if(r==4 && c==5 && m==8)
      printf("*****\n***..\n....c\n.....\n");
    if(r==4 && c==5 && m==9)
      printf("*****\n**...\n*..c.\n*....\n");
    if(r==4 && c==5 && m==10)
      printf("*****\n*****\n.....\nc....\n");
    if(r==4 && c==5 && m==11)
      printf("*****\n**...\n**.c.\n**...\n");
    if(r==4 && c==5 && m==12)
      printf("*****\n*****\n*....\n*.c..\n");
    if(r==4 && c==5 && m==13)
      printf("Impossible\n");
    if(r==4 && c==5 && m==14)
      printf("*****\n*****\n**...\n**.c.\n");
    if(r==4 && c==5 && m==15)
      printf("Impossible\n");
    if(r==4 && c==5 && m==16)
      printf("*****\n*****\n***..\n***.c\n");
    if(r==4 && c==5 && m==17)
      printf("Impossible\n");
    if(r==4 && c==5 && m==18)
      printf("Impossible\n");
    if(r==4 && c==5 && m==19)
      printf("*****\n*****\n*****\n****c\n");
    if(r==5 && c==1 && m==0)
      printf("c\n.\n.\n.\n.\n");
    if(r==5 && c==1 && m==1)
      printf("*\n.\nc\n.\n.\n");
    if(r==5 && c==1 && m==2)
      printf("*\n*\n.\nc\n.\n");
    if(r==5 && c==1 && m==3)
      printf("*\n*\n*\n.\nc\n");
    if(r==5 && c==1 && m==4)
      printf("*\n*\n*\n*\nc\n");
    if(r==5 && c==2 && m==0)
      printf("c.\n..\n..\n..\n..\n");
    if(r==5 && c==2 && m==1)
      printf("Impossible\n");
    if(r==5 && c==2 && m==2)
      printf("**\n..\nc.\n..\n..\n");
    if(r==5 && c==2 && m==3)
      printf("Impossible\n");
    if(r==5 && c==2 && m==4)
      printf("**\n**\n..\nc.\n..\n");
    if(r==5 && c==2 && m==5)
      printf("Impossible\n");
    if(r==5 && c==2 && m==6)
      printf("**\n**\n**\n..\nc.\n");
    if(r==5 && c==2 && m==7)
      printf("Impossible\n");
    if(r==5 && c==2 && m==8)
      printf("Impossible\n");
    if(r==5 && c==2 && m==9)
      printf("**\n**\n**\n**\n*c\n");
    if(r==5 && c==3 && m==0)
      printf("c..\n...\n...\n...\n...\n");
    if(r==5 && c==3 && m==1)
      printf("*.c\n...\n...\n...\n...\n");
    if(r==5 && c==3 && m==2)
      printf("*.c\n*..\n...\n...\n...\n");
    if(r==5 && c==3 && m==3)
      printf("***\n...\nc..\n...\n...\n");
    if(r==5 && c==3 && m==4)
      printf("***\n*..\n..c\n...\n...\n");
    if(r==5 && c==3 && m==5)
      printf("***\n*..\n*.c\n...\n...\n");
    if(r==5 && c==3 && m==6)
      printf("***\n***\n...\nc..\n...\n");
    if(r==5 && c==3 && m==7)
      printf("***\n***\n*..\n..c\n...\n");
    if(r==5 && c==3 && m==8)
      printf("Impossible\n");
    if(r==5 && c==3 && m==9)
      printf("***\n***\n***\n...\nc..\n");
    if(r==5 && c==3 && m==10)
      printf("Impossible\n");
    if(r==5 && c==3 && m==11)
      printf("***\n***\n***\n*..\n*.c\n");
    if(r==5 && c==3 && m==12)
      printf("Impossible\n");
    if(r==5 && c==3 && m==13)
      printf("Impossible\n");
    if(r==5 && c==3 && m==14)
      printf("***\n***\n***\n***\n**c\n");
    if(r==5 && c==4 && m==0)
      printf("c...\n....\n....\n....\n....\n");
    if(r==5 && c==4 && m==1)
      printf("*.c.\n....\n....\n....\n....\n");
    if(r==5 && c==4 && m==2)
      printf("**.c\n....\n....\n....\n....\n");
    if(r==5 && c==4 && m==3)
      printf("**.c\n*...\n....\n....\n....\n");
    if(r==5 && c==4 && m==4)
      printf("****\n....\nc...\n....\n....\n");
    if(r==5 && c==4 && m==5)
      printf("****\n*...\n..c.\n....\n....\n");
    if(r==5 && c==4 && m==6)
      printf("****\n**..\n...c\n....\n....\n");
    if(r==5 && c==4 && m==7)
      printf("****\n**..\n*..c\n....\n....\n");
    if(r==5 && c==4 && m==8)
      printf("****\n****\n....\nc...\n....\n");
    if(r==5 && c==4 && m==9)
      printf("****\n****\n*...\n..c.\n....\n");
    if(r==5 && c==4 && m==10)
      printf("****\n****\n**..\n...c\n....\n");
    if(r==5 && c==4 && m==11)
      printf("****\n****\n*...\n*.c.\n*...\n");
    if(r==5 && c==4 && m==12)
      printf("****\n****\n****\n....\nc...\n");
    if(r==5 && c==4 && m==13)
      printf("Impossible\n");
    if(r==5 && c==4 && m==14)
      printf("****\n****\n****\n*...\n*.c.\n");
    if(r==5 && c==4 && m==15)
      printf("Impossible\n");
    if(r==5 && c==4 && m==16)
      printf("****\n****\n****\n**..\n**.c\n");
    if(r==5 && c==4 && m==17)
      printf("Impossible\n");
    if(r==5 && c==4 && m==18)
      printf("Impossible\n");
    if(r==5 && c==4 && m==19)
      printf("****\n****\n****\n****\n***c\n");
    if(r==5 && c==5 && m==0)
      printf("c....\n.....\n.....\n.....\n.....\n");
    if(r==5 && c==5 && m==1)
      printf("*.c..\n.....\n.....\n.....\n.....\n");
    if(r==5 && c==5 && m==2)
      printf("**.c.\n.....\n.....\n.....\n.....\n");
    if(r==5 && c==5 && m==3)
      printf("***.c\n.....\n.....\n.....\n.....\n");
    if(r==5 && c==5 && m==4)
      printf("***.c\n*....\n.....\n.....\n.....\n");
    if(r==5 && c==5 && m==5)
      printf("*****\n.....\nc....\n.....\n.....\n");
    if(r==5 && c==5 && m==6)
      printf("*****\n*....\n..c..\n.....\n.....\n");
    if(r==5 && c==5 && m==7)
      printf("*****\n**...\n...c.\n.....\n.....\n");
    if(r==5 && c==5 && m==8)
      printf("*****\n***..\n....c\n.....\n.....\n");
    if(r==5 && c==5 && m==9)
      printf("*****\n***..\n*...c\n.....\n.....\n");
    if(r==5 && c==5 && m==10)
      printf("*****\n*****\n.....\nc....\n.....\n");
    if(r==5 && c==5 && m==11)
      printf("*****\n*****\n*....\n..c..\n.....\n");
    if(r==5 && c==5 && m==12)
      printf("*****\n*****\n**...\n...c.\n.....\n");
    if(r==5 && c==5 && m==13)
      printf("*****\n*****\n***..\n....c\n.....\n");
    if(r==5 && c==5 && m==14)
      printf("*****\n*****\n**...\n*..c.\n*....\n");
    if(r==5 && c==5 && m==15)
      printf("*****\n*****\n*****\n.....\nc....\n");
    if(r==5 && c==5 && m==16)
      printf("*****\n*****\n**...\n**.c.\n**...\n");
    if(r==5 && c==5 && m==17)
      printf("*****\n*****\n*****\n*....\n*.c..\n");
    if(r==5 && c==5 && m==18)
      printf("Impossible\n");
    if(r==5 && c==5 && m==19)
      printf("*****\n*****\n*****\n**...\n**.c.\n");
    if(r==5 && c==5 && m==20)
      printf("Impossible\n");
    if(r==5 && c==5 && m==21)
      printf("*****\n*****\n*****\n***..\n***.c\n");
    if(r==5 && c==5 && m==22)
      printf("Impossible\n");
    if(r==5 && c==5 && m==23)
      printf("Impossible\n");
    if(r==5 && c==5 && m==24)
      printf("*****\n*****\n*****\n*****\n****c\n");
  }
}
