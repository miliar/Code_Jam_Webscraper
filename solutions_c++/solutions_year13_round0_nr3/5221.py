#include<iostream>
#include<cmath>


using namespace std;

int main()
{
long long int afair, num[20], cont=1, resps = 0, frag, num2, i, j, k, aux, n1, n2, tam, auxxx;
long long int tam1, tam2;


cin >> afair;

while(afair--)
{
cin >> n1 >> n2;

resps = 0;
for(i=n1; i<=n2; i++)
{
frag = 1;
aux = i;
j = 0;
while(aux > 0)
{
num[j] = aux%10;
aux= aux/10;
j++;
}

k = j/2;

j--;
for(tam = 0; tam<k; tam++, j--)
{
if(num[tam] != num[j])
{
frag = 0;

break;
}
}


if(frag == 0)
continue;

else
{
num2 = sqrt(i);
if((num2*num2) == i)
{
j =0;
auxxx = num2;
while(auxxx > 0)
{
num[j] = auxxx%10;
auxxx= auxxx/10;
j++;
}
k = j/2;
j--;
for(tam = 0; tam<k; tam++, j--)
{
if(num[tam] != num[j])
{
frag = 0;
break;
}
}

if(frag == 1)
resps++;
}
}
}

cout << "Case #" << cont << ": " << resps << endl;
cont++;
}
return 0;
}
