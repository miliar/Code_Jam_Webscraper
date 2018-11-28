
//----------------------------------------------------------------------------
// Require-header-file(s)
//----------------------------------------------------------------------------

// Standard-library
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

//----------------------------------------------------------------------------
// Common using types
//----------------------------------------------------------------------------

typedef size_t                               size_type;
typedef std::vector< size_type >             list_type;
typedef char                                 char_type;
typedef std::basic_string< char_type >       bstr_type;
typedef std::basic_ifstream< char_type >     ifst_type;
typedef std::basic_ofstream< char_type >     ofst_type;
typedef std::basic_stringstream< char_type > sstr_type;

//----------------------------------------------------------------------------
//! \brief Check if the input number is a palindrome.
//! \param value Value to be checked.
//! \return True if the input number is a palindrome.
//----------------------------------------------------------------------------

bool is_palindrome( size_type value )
{
  sstr_type sstr;
  if( false == !!(sstr << value) )
    return false;

  bstr_type text = sstr.str( );
  size_type size = text.size( );
  for( size_type i = 0; i < size / 2; ++i )
  {
    if( text[i] != text[size - i - 1] )
      return false;
  }

  return true;
}

//----------------------------------------------------------------------------
//! \brief Make the list of palindrome.
//! \param minv Minimum value to be generated.
//! \param maxv Maximum value to be generated.
//! \return True if there is no error occured.
//----------------------------------------------------------------------------

bool make_list( size_type   minv,
                size_type   maxv,
                list_type & list )
{
  for( size_type i = minv; i <= maxv; ++i )
  {
    size_type j = static_cast< size_type >( std::sqrt( i ) );
    if( i != (j * j) )
      continue;

    if( true == is_palindrome( i ) )
    {
      if( true == is_palindrome( j ) )
        list.push_back( i );
    }
  }

  return true;
}

//----------------------------------------------------------------------------
//! \brief Main entrance of this program.
//! \param argc, number of input arguments.
//! \param argv, list of input arguments.
//! \return 0 if program exits successfully.
//----------------------------------------------------------------------------

int main( int     argc, 
          char ** argv )
{
  char const * file_i = argv[1];
  char const * file_o = argv[2];
  if( argc != 3 )
  {
    std::wcerr << "Usage: ./run.out <input-file> <output-file>" << std::endl;
    return 1;
  }

  list_type list;
  if( false == make_list( 1, 1000, list ) )
  {
    std::wcerr << "Error: Unable to make the list." << std::endl;
    return 1;
  }

  // for( size_type i = 0; i < list.size( ); ++i )
  //  std::cout << "> " << list[i] << std::endl;

  ifst_type ifst( file_i );
  if( false == ifst.is_open( ) )
  {
    std::wcerr << "Error: Unable to open file '" << file_i << "'." << std::endl;
    return 1;
  }

  ofst_type ofst( file_o );
  if( false == ofst.is_open( ) )
  {
    std::wcerr << "Error: Unable to create file '" << file_o << "'." << std::endl;
    return 1;
  }

  size_type loop = 0;
  if( false == !!(ifst >> loop) )
  {
    std::wcerr << "Error: Found invalid number of loops." << std::endl;
    return 1;
  }

  size_type a, b;
  for( size_type l = 0; l < loop; ++l )
  {
    if( false == !!(ifst >> a >> b) )
    {
      std::wcerr << "Error: Found invalid inputs in loop #" << l << "." << std::endl;
      return 1;
    }

    size_type i = 0, j = 0;
    {
      for( i = 0; i < list.size( ); ++i )
      {
        if( a <= list[i] )
          break;
      }

      for( j = 0; j < list.size( ); ++j )
      {
        if( b < list[j] )
          break;
      }
    }

    ofst << "Case #" << (l+1) << ": " << (j - i) << std::endl;
  }

  return 0;
}

//----------------------------------------------------------------------------
// End-of-file
//----------------------------------------------------------------------------

