#include <bits/stdc++.h>
using namespace std;


    vector<char> letras;

void insertarDelante(char a){
    
   letras.push_back(a);
}
void insertarDestras(char a)
{
     vector<char> temp;
    for(int i=0;i<letras.size();i++)
        temp.push_back(letras[i]);
    letras.clear();
    letras.push_back(a);
    for(int i=0;i<temp.size();i++)
    {
        letras.push_back(temp[i]);
    }
}
int main()
{
    int casos;
    scanf("%d\n",&casos);
    char buffer[4000];
    for(int caso=1;caso<=casos;caso++)
    {
        letras.clear();
        gets(buffer);
        int len = strlen(buffer);
        
        int right =(int)buffer[0];
        int left=(int)buffer[0];
        letras.push_back(buffer[0]);
        for(int i=1;i<len;i++)
        {
            if(buffer[i]>=left)
            {
                insertarDestras(buffer[i]);
                left = (int)buffer[i];
            }
            else
            {
                insertarDelante(buffer[i]);
            }
        }
        printf("Case #%d: ",caso);
        for(int i=0;i<len;i++)
        {
            printf("%c",letras[i]);
        }
        printf("\n");
        
    }
    return 0;
}
