#include <fstream>

using namespace std;

int main()
{
    ifstream cin( "input.txt" );
    ofstream cout( "output.txt" );
    
    int n;
    cin >> n;
    
    for( int i=0; i<n; i++ )
    {
    	int m[16] = { 0 };
		
		int num;
    	cin >> num;
    	
    	char buf[50];
		cin.getline( buf, 50 );
    	
    	for( int j=1; j<=4; j++ )
    		if( j == num )
    		{
    			for( int t=0; t<4; t++ )
    			{
    				int b;
    				cin >> b;
    				
    				m[b-1]++;
    			}
    			
    			cin.getline( buf, 50 );
    		}
    		else
				cin.getline( buf, 50 );
			
		cin >> num;
		
		cin.getline( buf, 50 );
    	
    	for( int j=1; j<=4; j++ )
    		if( j == num )
    		{
    			for( int t=0; t<4; t++ )
    			{
    				int b;
    				cin >> b;
    				
    				m[b-1]++;
    			}
    			
    			cin.getline( buf, 50 );
    		}
    		else
				cin.getline( buf, 50 );
				
			int otv = 0, acc = 0;
			bool norm = true;
    			
    		for( int j=0; j<16; j++ )
    		{
    			if( m[j] )
    				acc++;
				
				if( m[j] == 2 )
    				otv = j+1;
    				
    			if( m[j] > 2 )
    				norm = false;
    		}
    		
    		cout << "Case #" << i+1 << ": ";
    		
    		if( acc == 8 )
    			cout << "Volunteer cheated!";
    		else
    		if( acc < 7 || !norm )
    			cout << "Bad magician!";
    		else
    			cout << otv;
    			
    		cout << endl;
    }
}
