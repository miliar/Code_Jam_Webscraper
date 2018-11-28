#include <iostream>
#include <string>

using namespace std;

int main()
{
    int test;
    cin>>test;
    int caso=1;

    while(test-->0)
    {
        int n;
        cin>>n;

        char pessoas[n+1];
        int vetor[n+1];

        for(int i=0;i<=n;i++)
        {
            cin>>pessoas[i];
        }

        for(int i=0;i<=n;i++)
            vetor[i]=pessoas[i]-48;


        int amigos_necessarios=0;
        for(int i=1;i<n+1;i++){
            int cont_parcial=0;
            for(int j=0;j<i;j++){
                cont_parcial+=vetor[j];
            }
            cont_parcial+=amigos_necessarios;
            while(cont_parcial<i){
                cont_parcial++;
                amigos_necessarios++;
            }
        }


        cout<<"Case #"<<caso++<<": "<<amigos_necessarios<<endl;

        }


    return 0;
}
