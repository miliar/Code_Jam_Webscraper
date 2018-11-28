#include <iostream>

using namespace std;


int *v1=new int[4],*v2=new int[4];
int card;
int repete()
{
    int i,j,c=0;
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            if(v1[i]==v2[j])
            {
                c++;
                card=v1[i];
            }
        }

    }
    if(c==1)
        return 1;
    if(c>1)
        return 2;
    if(c==0)
        return 3;


}

int main()
{
    int N,i,j,it=1,b,linha;
    int resp;
    cin >> N;
    while (it<=N)
    {
        cin >> linha;
        for (i=0; i<4; i++)
        {
            for (j=0; j<4; j++)
            {
                cin >> b;
                if(i==linha-1)
                    v1[j] = b;
            }
        }
        cin >> linha;
        for (i=0; i<4; i++)
        {
            for (j=0; j<4; j++)
            {
                cin >> b;
                if(i==linha-1)
                    v2[j] = b;
            }
        }
        resp = repete();
        cout << "Case #" << it++ <<": ";
        if (resp==1)
        {
            cout<<card<<endl;
        }
        else
        {
            if (resp==2)
            {
                cout<<"Bad magician!"<<endl;
            }
            else
            {
                if (resp==3)
                {
                    cout<<"Volunteer cheated!"<<endl;
                }
            }
        }

    }
    return 0;
}
