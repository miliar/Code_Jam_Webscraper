#include <bits/stdc++.h>
using namespace std;
char word[5000];
int main()
{
    list<char> m_list;
    int T;
    scanf("%d \n", &T);
    for(int t = 1; t<=T; t++)
    {
        scanf(" %s", word);
        int n = strlen(word);
        m_list.clear();
        m_list.push_front(word[0]);
        for(int i = 1; i<n; i++)
        {
            if(word[i]>=m_list.front()) m_list.push_front(word[i]);
            else m_list.push_back(word[i]);
        }
        printf("Case #%d: ", t);
        for(list<char>::iterator i = m_list.begin(); i!=m_list.end(); i++)
        {
            printf("%c", (*i));
        }
        printf("\n");
    }
}
