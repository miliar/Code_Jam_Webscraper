#include <iostream>
using namespace std;

int main()
{
    int T, Smax, result;
    char ch;
    FILE *fp;
    fp = fopen("ProblemA.txt", "a");
    cin >> T;
    for (int count = 1; count <= T; count++)
    {
        result = 0;
        int ch_i, sum = 0;
        
        cin >> Smax;
        
        // ��Ӧ�ڵ�һ������ 
        cin >> ch;
        ch_i = ch - '0';
        sum += ch_i;
        
        for (int i = 0; i < Smax; i++)
        {// �����forѭ����˵��Smax >= 1����ô�������������֣�����������ʼ��iȡ0ֵʱ���൱�ھ��ǿ��ǵڶ�������x1�ˣ���result >= 1 - x0
            // ��������x(i+1)��result >= 1 - (x0 + ... + xi) 
            if (result < i+1 - sum) // �����sum�͵���x0 + ... + xi
            {
                result = i+1 - sum;
            }
            cin >> ch;
            ch_i = ch - '0';
            sum += ch_i;
        }
        cout << "Case #" << count << ": " << result << endl;
        fprintf(fp, "Case #%d: %d\n", count, result);  
    }
    fclose(fp);
}
