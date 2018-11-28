#include <bits/stdc++.h>


using namespace std;
typedef struct info {

int numOfElements;
int numOfDashes;
int numOfPluses;
};
info manipulateTheElements (char A[])
{
    info KAYYY;
     int countele=0,countdash=0,countplus=0;
    for (int i=0;i<strlen(A);i++)
    {


        if (A[i]=='-')
        {
          countele++;
          countdash++;
        }
        else {
            countele++;
            countplus++;
        }
    }

    KAYYY.numOfDashes=countdash;
    KAYYY.numOfElements=countele;
    KAYYY.numOfPluses=countplus;
    return KAYYY;
}
bool check (char A[])
{
    int pluses=0;
    for (int k=0;k<strlen(A);k++)
    {
        if (A[k]=='+')
        {
            pluses++;
        }
    }
    if (pluses==strlen(A))
    {
        return true;
    }
    else {
        return false;
    }
}

int main ()
{
    ifstream in("B-large.in");
    ofstream out("output.txt");
    char A[102]={'\0'};
    int n,counttries=0,index=0;
    info hola;
    in >> n;
    int m=n;
    vector <int> a(n);
    while (n>0)
    {
        in >> A;
        hola=manipulateTheElements(A);
        if (hola.numOfDashes==hola.numOfElements)
        {
            a[index]=1;
            index++;
        }
        else if (hola.numOfPluses==hola.numOfElements)
        {
            a[index]=0;
            index++;
        }
        else {
        while (check(A)==false){
        if (A[0]=='+'){
            for (int i=1;i<strlen(A);i++)
        {
            if (A[i]!='+'){
            i--;
                reverse(A,A+i);
                 for (int j=0;j<=i;j++)
                 {
                     if (A[j]=='-')
                     {
                         A[j]='+';
                     }
                     else {
                        A[j]='-';
                     }
                 }
           counttries++;
           if (check(A)==true)
           {
               break;
           }
           if (A[0]=='-')
           {
               break;
           }
        }

        }
        }
        else if (A[0]=='-')
        {
            for (int i=strlen(A)-1;i>=0;i--)
            {
                if (A[i]=='-')
                {
                    reverse(A,A+(i+1));
                    for (int j=0;j<=i;j++)
                 {
                     if (A[j]=='-')
                     {
                         A[j]='+';
                     }
                     else {
                        A[j]='-';
                     }

                 }
                 counttries++;
                 if (check(A)==true)
           {
               break;
           }
           if (A[0]=='+')
           {
               break;
           }
                }


        }
                }
            }

            a[index]=counttries;
            index++;
            counttries=0;

        }
        n--;
}
for (int i=0;i<m;i++)
{
    out <<"Case #" <<i+1<<": " <<a[i] << endl;
}
}



