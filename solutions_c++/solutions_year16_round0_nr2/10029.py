    int main()
    {
        int T;
        cin >> T;
        
        
        //for ( int k = 0; k < 108; k++ )
          //  cout << k << endl;
        
        
        for ( int j = 1; j <= T; j++ )
        {
            
            int counter = 0;
            
            string S;
            cin >> S;
            
            for ( int i = 0; i < S.length(); i++ )
            {
                if ( S[ i ] == S[ i - 1 ] )
                    counter--;
                
            
                counter++;
            } // end inner for
            if ( S[S.length() -1 ] == '+' )
                counter--;
            cout << "\nCase #" << j << ": " << counter;
        } // end outer for
        
        
        
        
        
        return 0;
    } // end main