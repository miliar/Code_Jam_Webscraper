#include<iostream>
#include<vector>

using namespace std;


class Game
{
    private:

    public:
        int m_test_case_number;

        int m_A;
        int m_B;
        int m_K;

        int m_win_count;

        Game()
        {
            m_test_case_number=0;
            m_win_count=0;
        }

        void readData()
        {
            cin>>m_A;
            cin>>m_B;
            cin>>m_K;
        }


        int setTestCaseNumber(int arg_no)
        {
            m_test_case_number = arg_no;
        }
        int getTestCase()
        {
            return m_test_case_number;
        }
        int getWinCount()
        {
            return m_win_count;
        }

        void processWin()
        {
            int temp_and;
            for(int i = 0; i < m_A; i++)
            {
                for(int j = 0; j < m_B; j++)
                {
                    temp_and = i&j;
                    if( temp_and < m_K )
                    {
                        m_win_count++;
                    }
                }
            }
        }
};


int main()
{
    int m_test_count=0;

    cin>>m_test_count;

    vector<Game> m_test_cases;

    for(int i=1;i<=m_test_count;i++)
    {
        Game t_game;
        t_game.setTestCaseNumber(i);
        t_game.readData();
        t_game.processWin();

        m_test_cases.push_back(t_game);
    }
    for(int i=0;i<m_test_cases.size(); i++)
    {
        cout<<"Case "<<"#"<<m_test_cases.at(i).getTestCase()<<": "<<m_test_cases.at(i).getWinCount();
        cout<<endl;
    }



}
