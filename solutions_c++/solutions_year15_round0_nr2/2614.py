#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int melhor(vector<int> vetor);

int main()
{
    int t,d,aux,result;
    vector<int> p;

    scanf("%d",&t);
    for(int i = 0 ; i < t ; i++)
    {
        scanf("%d",&d);

        for(int j = 0 ; j < d ; j++)
        {
            scanf("%d ",&aux);
            p.push_back(aux);
        }

        result = melhor(p);

        printf("Case #%d: %d\n",i+1,result);

        p.clear();
    }

    return 0;
}

int melhor(vector<int> vetor)
{
    sort(vetor.begin(),vetor.end());
    vector<int> vetorMopa = vetor;
    int result,temp;

    result = vetorMopa.back();
    for(int i = 2; i <= vetorMopa.back() / 2 ; i++)
    {
        temp = vetorMopa.back();
        vetorMopa.pop_back();
        vetorMopa.push_back(temp - i);
        vetorMopa.push_back(i);
        //sort(vetorMopa.begin(),vetorMopa.end());

        result = min(result,1 + melhor(vetorMopa));
        vetorMopa = vetor;
    }

    return result;
}
