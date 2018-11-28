#include <iostream>
using namespace std;
int main()
{
    int num;
    cin>>num;
    int cont=0;
    for(int i=0; i<num; i++)
    {
        cont++;
        int cant;
        cin>>cant;
        string s;
        cin>>s;
        int total=0;
        int arr[cant+1];
        for(int j=0; j<=s.size(); j++)
        {
            if(s[j]=='0')
            {
                arr[j]=0;
            }
            if(s[j]=='1')
            {
                arr[j]=1;
            }
            if(s[j]=='2')
            {
                arr[j]=2;
            }
            if(s[j]=='3')
            {
                arr[j]=3;
            }
            if(s[j]=='4')
            {
                arr[j]=4;
            }
            if(s[j]=='5')
            {
                arr[j]=5;
            }
            if(s[j]=='6')
            {
                arr[j]=6;
            }
            if(s[j]=='7')
            {
                arr[j]=7;
            }
            if(s[j]=='8')
            {
                arr[j]=8;
            }
            if(s[j]=='9')
            {
                arr[j]=9;
            }

        }
        int suma=arr[0];
        for(int j=1; j<cant+1; j++)
        {
            if(arr[j]!=0)
            {
                if(j>suma)
                {

                    total+=j-suma;
                    suma+=total;

                }

                suma=suma+arr[j];

            }
        }
        cout<<"Case #"<<cont<<": "<<total<<endl;


    }




    return 0;
}
