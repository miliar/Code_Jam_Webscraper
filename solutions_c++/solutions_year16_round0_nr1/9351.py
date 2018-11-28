#include <bits/stdc++.h>

using namespace std;
bool check[10]={false};
void clearing(){

for (int i=0;i<10 ;i++)
{
    if (check[i]==true)
    {
        check[i]=false;
    }
}



}

bool checker(int num)
{
    unsigned long long int temp,counter=0;

    while (num>0)
    {


           temp=num%10;
           num=num/10;


        if (temp==0)
        {
            check[0]=true;
        }
        if (temp==1)
        {
            check[1]=true;
        }
        if (temp==2 )
        {
            check[2]=true;
        }
        if (temp==3)
        {
            check[3]=true;
        }
        if (temp==4)
        {
            check[4]=true;
        }
        if (temp==5)
        {
            check[5]=true;
        }
        if (temp==6)
        {
            check[6]=true;
        }
        if (temp==7)
        {
            check[7]=true;
        }
        if (temp==8)
        {
            check[8]=true;
        }
         if (temp==9)
        {
            check[9]=true;
        }
    }
    ///count the truezzz
        for (int i=0 ; i<10 ;i++)
        {
            if (check[i]==true)
            {
                counter++;
            }
        }
        if (counter==10)
        {
            return true;
        }
        else {
            return false;
        }
}
int main()
{
    ifstream in("A-large.in");
    ofstream out("output.txt");
   unsigned long long int n,num,i,order=1;
bool y=false;
   in >> n;
   while (n!=0){

       in >> num;
       if (num==0)
       {
        out << "Case #"<< order <<": INSOMNIA" << endl;
           order++;

       }
       else{
       for ( i=1;y==false;i++){
        y=checker(num*i);
       }
        out <<"Case #" << order <<": " << num*(i-1) << endl;
        order++;
       }
        n--;
        y=false;
        clearing();

   }
//         in.close();
//        out.close();
}
