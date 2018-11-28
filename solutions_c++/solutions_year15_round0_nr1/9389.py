using namespace std;
#include<iostream>
#include<fstream>


inline int num(char ch){
switch(ch){

case '0': return 0;
case '1': return 1;
case '2': return 2;
case '3': return 3;
case '4': return 4;
case '5': return 5;
case '6': return 6;
case '7': return 7;
case '8': return 8;
case '9': return 9;
default : return 0;


}

}

int main()
{
    ofstream myfile;
    myfile.open ("examplenew.txt");
    int T=0;
    char ch;
    int k=0,J=0,c=0;
    int M=0,counter=0;
    int a=0;

    cin>>T;

    while(counter<T)
    {
        J=0;
        k=0;
        c=0;
        cin>>M;
        //cin.get(ch);

        while(c<=M)
        {
            if(k>=c)
            {
                c++;
                //read a
                cin>>ch;
                a=num(ch);


                k+=a;
            }
            else
            {
                 cin>>ch;
                a=num(ch);

                while(a==0 && c<=M)
                {
                    c++;
                     cin>>ch;
                a=num(ch);

                }

                if(c<=M)
                {
                    J+=c-k;
                    k=c+a;
                    c++;
                }




            }




        }

        counter++;
        myfile<<"Case #"<<counter<<": "<<J<<endl;



    }


myfile.close();

}
